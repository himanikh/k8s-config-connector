/**
 * Copyright 2022 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

```hcl
resource "google_bigquery_dataset" "public" {
  dataset_id                  = "public"
  friendly_name               = "test"
  description                 = "This dataset is public"
  location                    = "EU"
  default_table_expiration_ms = 3600000

  labels = {
    env = "default"
  }

  access {
    role          = "OWNER"
    user_by_email = google_service_account.bqowner.email
  }

  access {
    role   = "READER"
    domain = "hashicorp.com"
  }
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "private"
  friendly_name               = "test"
  description                 = "This dataset is private"
  location                    = "EU"
  default_table_expiration_ms = 3600000

  labels = {
    env = "default"
  }

  access {
    role          = "OWNER"
    user_by_email = google_service_account.bqowner.email
  }

  access {
    role   = "READER"
    domain = "hashicorp.com"
  }

  access {
    dataset {
      dataset {
        project_id = google_bigquery_dataset.public.project
        dataset_id = google_bigquery_dataset.public.dataset_id
      }
      target_types = ["VIEWS"]
    }
  }
}

resource "google_service_account" "bqowner" {
  account_id = "bqowner"
}
```
