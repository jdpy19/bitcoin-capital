# POC-3: Bech32 addresses are not accepted by the backend (BUG)

```
TAGS: backend, live, bitcoin
```

Bech32 addresses are not accepted by the backend.

## To Reproduce

1. Create a new list
2. Attempt to add a Bech32 address (e.g. - `bc1qms4wpag0pemty2nk4ahtw4tfs089e0g7yjn5sh`)
3. See the error message claiming the address is not valid
