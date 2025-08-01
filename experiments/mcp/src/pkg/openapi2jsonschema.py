#!/usr/bin/env python3
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yaml
import json
import sys
import os
import urllib.request
      
def run(crdFile):
    files = []

    if crdFile.startswith("http"):
        f = urllib.request.urlopen(crdFile)
    else:
        f = open(crdFile)
   
    with f:
        defs = []
        yaml.SafeLoader.add_constructor(u'tag:yaml.org,2002:value', construct_value)
        for y in yaml.load_all(f, Loader=yaml.SafeLoader):
            if y is None:
                continue
            if "items" in y:
                defs.extend(y["items"])
            if "kind" not in y:
                continue
            if y["kind"] != "CustomResourceDefinition":
                continue
            else:
                defs.append(y)

        for y in defs:
            filename_format = os.getenv("FILENAME_FORMAT", "{kind}_{version}")
            filename = ""
            if "spec" in y and "versions" in y["spec"] and y["spec"]["versions"]:
                for version in y["spec"]["versions"]:
                    if "schema" in version and "openAPIV3Schema" in version["schema"]:
                        filename = filename_format.format(
                            kind=y["spec"]["names"]["kind"],
                            group=y["spec"]["group"].split(".")[0],
                            fullgroup=y["spec"]["group"],
                            version=version["name"],
                        ).lower() + ".json"

                        schema = version["schema"]["openAPIV3Schema"]
                        write_schema_file(schema, filename)
                        files.append(filename)
                    elif "validation" in y["spec"] and "openAPIV3Schema" in y["spec"]["validation"]:
                        filename = filename_format.format(
                            kind=y["spec"]["names"]["kind"],
                            group=y["spec"]["group"].split(".")[0],
                            fullgroup=y["spec"]["group"],
                            version=version["name"],
                        ).lower() + ".json"

                        schema = y["spec"]["validation"]["openAPIV3Schema"]
                        write_schema_file(schema, filename)
                        files.append(filename)

            elif "spec" in y and "validation" in y["spec"] and "openAPIV3Schema" in y["spec"]["validation"]:
                filename = filename_format.format(
                    kind=y["spec"]["names"]["kind"],
                    group=y["spec"]["group"].split(".")[0],
                    fullgroup=y["spec"]["group"],
                    version=y["spec"]["version"],
                ).lower() + ".json"

                schema = y["spec"]["validation"]["openAPIV3Schema"]
                write_schema_file(schema, filename)
                files.append(filename)
                      
    return files


def additional_properties(data, skip=False):
    if isinstance(data, dict):
        if "properties" in data and not skip:
            if "additionalProperties" not in data:
                data["additionalProperties"] = False
        for _, v in data.items():
            additional_properties(v)
    return data

def replace_int_or_string(data):
    new = {}
    try:
        for k, v in iter(data.items()):
            new_v = v
            if isinstance(v, dict):
                if "format" in v and v["format"] == "int-or-string":
                    new_v = {"oneOf": [{"type": "string"}, {"type": "integer"}]}
                else:
                    new_v = replace_int_or_string(v)
            elif isinstance(v, list):
                new_v = list()
                for x in v:
                    new_v.append(replace_int_or_string(x))
            else:
                new_v = v
            new[k] = new_v
        return new
    except AttributeError:
        return data

def allow_null_optional_fields(data, parent=None, grand_parent=None, key=None):
    new = {}
    try:
        for k, v in iter(data.items()):
            new_v = v
            if isinstance(v, dict):
                new_v = allow_null_optional_fields(v, data, parent, k)
            elif isinstance(v, list):
                new_v = list()
                for x in v:
                    new_v.append(allow_null_optional_fields(x, v, parent, k))
            elif isinstance(v, str):
                is_non_null_type = k == "type" and v != "null"
                has_required_fields = grand_parent and "required" in grand_parent
                if is_non_null_type and not has_required_fields:
                    new_v = [v, "null"]
            new[k] = new_v
        return new
    except AttributeError:
        return data


def append_no_duplicates(obj, key, value):
    """
    Given a dictionary, lookup the given key, if it doesn't exist create a new array.
    Then check if the given value already exists in the array, if it doesn't add it.
    """
    if key not in obj:
        obj[key] = []
    if value not in obj[key]:
        obj[key].append(value)


def write_schema_file(schema, filename):
    schemaJSON = ""

    schema = additional_properties(schema, skip=not os.getenv("DENY_ROOT_ADDITIONAL_PROPERTIES"))
    schema = replace_int_or_string(schema)
    schemaJSON = json.dumps(schema, indent=2)

    # Dealing with user input here..
    filename = os.path.basename(filename)
    f = open(filename, "w")
    print(schemaJSON, file=f)
    f.close()
    print("JSON schema written to {filename}".format(filename=filename))

def construct_value(load, node):
    # Handle nodes that start with '='
    # See https://github.com/yaml/pyyaml/issues/89
    if not isinstance(node, yaml.ScalarNode):
        raise yaml.constructor.ConstructorError(
            "while constructing a value",
            node.start_mark,
            "expected a scalar, but found %s" % node.id, node.start_mark
        )
    yield str(node.value)
