# Signing and fees

**Short version:** each member authorises only their own step; Truway builds the transaction,
pays the fee and submits it, but cannot change what the member signed or sign for them. **On
testnet today, the platform holds demo signers** while per-person signing is built.

## How a member signs (design)

> Status: **Design.** Decided on 2026-11-07; the proof of concept is the gate before building.

1. The member clicks **Approve**.
2. The API builds the invocation `approve(approver, id)`, simulates it, takes the member's
   authorisation entry, sets its nonce and an expiry of about 720 ledgers (about one hour), and
   computes the hash to sign.
3. The browser signs that hash with the member's key, held by an embedded signer (Privy). There
   is no pop-up and no seed phrase.
4. The API checks the signature against the member's address, attaches it, simulates again, wraps
   the invocation in a transaction whose source and fee payer is Truway, signs the envelope and
   submits it through a queue.
5. The member sees *Approved*, then *Registered · verifiable*.

If submission fails, the API retries with a new envelope without asking again, while the
authorisation has not expired. The authorisation is bound to the exact arguments, so the server
cannot reuse it for something else.

## Who pays fees

Truway pays every network fee and rent. Members hold no XLM. This is what Stellar's documentation
calls fee sponsorship through a relayer: the user signs only the authorisation entries of their
contract call, and the relayer submits the transaction with its own account. Truway runs its own
serial queue today; [OpenZeppelin Relayer](https://developers.stellar.org/docs/tools/openzeppelin-relayer)
with its Channels plugin is the documented option for parallel submission and automatic fee bumps.

## Accounts

| Account | What it is for | Who holds the key |
|---|---|---|
| **Member's account** | Proposes and approves in their organisation's treasury | The member, through an embedded signer; Truway cannot sign for them (design) |
| **Demo signer** | Stands in for a member on testnet | The platform. Labelled *Demo signer*. Never on mainnet |
| **Own account** | For people who already use a Stellar wallet; signs in with a challenge (SEP-10) | The person |
| **Truway submitter** | Pays fees and submits | Truway |
| **Deployer** | Creates a new treasury; used once; never a member | Truway |

## What the server can and cannot do

| Can | Cannot |
|---|---|
| Build, simulate and submit transactions | Change what a member signed |
| Pay fees | Approve, propose or reject for a member (design; today demo signers) |
| Delay or refuse to submit a signed step | Move funds, change members or upgrade a treasury |

## Later

If members move to contract accounts with passkeys (secp256r1, CAP-51), authentication with
services follows SEP-45. Not planned for the MVP.
