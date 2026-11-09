# Roadmap

What is planned, in order. Nothing here is built yet unless it says so. Dates depend on funding.

## Next

1. **Each person signs their own step**, from the browser, without handling keys. Demo signers
   disappear.
2. **Contracts from the public procurement portal.** Link a contract by its SECOP II ID and fill
   in agency, contractor, value, dates, supervisor and funding source automatically.
3. **One invoice, once, everywhere.** A shared registry of supporting documents across
   organisations, with electronic invoices identified by their tax authority ID (the CUFE in
   Colombia).
4. **Alerts for the supervisor**: expense over what is left in the line; invoice already reported.

## Then

5. **Field advances as money.** An approved advance is paid out through the Stellar Disbursement
   Platform; the team lead accounts for each purchase against it; what is not spent is returned.
   All under the same standard.
6. **Cash-out to pesos** through a local partner.
7. **Stronger governance for the contract**: several admins, a timelock on code changes, expiring
   proposals and a pause.
8. **Independent security review**, then **mainnet**.

## Later

- Proof of Spend `v1.0`, after public feedback, with a read-only reference indexer.
- Contracts still on SECOP I, for the municipalities that use it.
- Exports for public accounting and comptroller reporting.
- More country packs.

## The road to mainnet

| Step | Status |
|---|---|
| Two signers on every change; budgets per funding source; single-use documents; typed errors; standard events | Done |
| Testnet deployment under Truway-controlled keys, deployer outside the treasury | Done |
| Internal review | Done (2026-11-07) |
| Generated TypeScript client and deploy script | Done |
| Per-person signing in the app | Planned |
| Several admins, timelock, proposal expiry, pause | Planned |
| Verified builds visible on explorers | In progress |
| Independent security review | Planned |
| Mainnet deployment | Planned |
