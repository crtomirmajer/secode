# Secode

[![CircleCI](https://circleci.com/gh/crtomirmajer/secode/tree/master.svg?style=shield)](https://circleci.com/gh/crtomirmajer/secode/tree/master)

## About
**secode**, short for _secrets encode_, is a utility for `base64` encoding/decoding Kubernetes secrets.
It takes a `.yaml` file or a stream as an input and replaces values with `base64` encoded/decoded strings.

Also works with multiple `Secret` definitions per file - `kind: List` or  `---` separated.

**Requires Python 3+**

## Install

Using `pip3`:

`pip3 install git+http://github.com/crtomirmajer/secode.git`

## Usage

Run:

```bash
secode secrets.yaml > secrets_base64.yaml
```

on `secrets.yaml` containing:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: secret_1
type: Opaque
data:
  secret_val_1: 'this-is-secret-1'
  secret_val_2: 1337
  secret_val_3: v/pp;QTh|F%@G5,9g,%qeh9j+ubQ3dM\
```

to get `secrets_base64.yaml`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: secret_1
type: Opaque
data:
  secret_val_1: dGhpcy1pcy1zZWNyZXQtMQ==
  secret_val_2: MTMzNw==
  secret_val_3: di9wcDtRVGh8RiVARzUsOWcsJXFlaDlqK3ViUTNkTVw=
```

Use `-d` (`--decode`) flag to get the original:

```bash
secode secrets_base64.yaml -d
```

Pipe `kubectl get secret` output through `secode -d` to decode a deployed K8s secret on-the-fly:

```bash
kubectl get secret <name-of-the-secret> -o yaml | secode -d
```
