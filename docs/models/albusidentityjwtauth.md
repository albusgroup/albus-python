# AlbusIdentityJWTAuth

A short-lived identity token issued by Albus for the calling organization and invocation, sent as "Authorization: Bearer". Your server must trust the organization's issuer (the "issuer" of the Organization resource) and require the server "url" as the audience; the issuer publishes its signing keys at "<issuer>/.well-known/jwks.json".


<https://docs.albus.sh/guides/mcp-server-auth>


## Fields

| Field                           | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `type`                          | *Literal["albus_identity_jwt"]* | :heavy_check_mark:              | N/A                             |