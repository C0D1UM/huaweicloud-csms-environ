# huaweicloud-csms-environ

[![GitHub](https://img.shields.io/github/license/C0D1UM/huaweicloud-csms-environ)](https://github.com/C0D1UM/huaweicloud-csms-environ/blob/main/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/C0D1UM/huaweicloud-csms-environ/CI)](https://github.com/C0D1UM/huaweicloud-csms-environ/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/C0D1UM/huaweicloud-csms-environ/branch/main/graph/badge.svg?token=PN19DJ3SDF)](https://codecov.io/gh/C0D1UM/huaweicloud-csms-environ)
[![PyPI](https://img.shields.io/pypi/v/huaweicloud-csms-environ)](https://pypi.org/project/huaweicloud-csms-environ/)  
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/huaweicloud-csms-environ)](https://github.com/C0D1UM/huaweicloud-csms-environ)

## Installation

```bash
pip install huaweicloud-csms-environ
```

## Sample Usage

```python
import csms

# basic
csms.load_env('secret-name', region='ap-southeast-2')

# project id instead of region
csms.load_env('secret-name', project_id='project-id')

# using pure environment variables
csms.load_env()

# no environment variables
csms.load_env(
   'secret_name',
   access_key='access-key',
   secret_key='secret-key',
   region='ap-southeast-2',
)
```

## Environment Variables

| Key                          | SDK | Description                    |
| ---------------------------- | --- | ------------------------------ |
| `HUAWEICLOUD_SDK_AK`         | Yes | Access key of Huawei Cloud IAM |
| `HUAWEICLOUD_SDK_SK`         | Yes | Secret key of Huawei Cloud IAM |
| `HUAWEICLOUD_SDK_PROJECT_ID` | Yes | Huawei Cloud project ID        |
| `HUAWEICLOUD_REGION`         | No  | Huawei Cloud region            |
| `HUAWEICLOUD_SECRET_NAME`    | No  | CSMS secret name               |

> For more SDK variables, please see [this](https://github.com/huaweicloud/huaweicloud-sdk-python-v3#241-environment-variables-top).

## Development

### Requirements

- Docker
- Python
- Poetry

### Linting

```bash
make lint
```

### Testing

```bash
make test
```

### Fix Formatting

```bash
make yapf
```
