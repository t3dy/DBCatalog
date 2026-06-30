---
name: project_bookstore
description: Personal e-commerce storefront (SHOPSITE spec → Bookstore implementation) selling the user's books, MTG cards, and gear.
type: project
status: ACTIVE
tags: [ecommerce, nextjs, stripe, supabase]
---

# Project: Bookstore / SHOPSITE

**Location** · `C:\Dev\Bookstore` (impl) + `C:\Dev\SHOPSITE` (spec) — **Type** · e-commerce storefront — **Stack** · Next.js 14, TS, Tailwind, Supabase, Stripe, PayPal, Zustand — **Verified** · Bookstore `.next` build present (not re-run this session)

## What it is
A personal-use single-seller storefront (own books, MTG cards, gear). `SHOPSITE` is the completed `PROJECT_SPEC.md` + partial scaffold; `Bookstore` is the implementation with cart and Stripe + PayPal checkout.

## Architecture
Next.js app (Bookstore) with cart state in Zustand, Supabase backing, Stripe + PayPal checkout. `SHOPSITE` holds the multi-category spec and an early `src/` predecessor.

## Fragile parts
Depends on env secrets (`.env.example`: Stripe/PayPal/Supabase keys) — not committed, so builds need setup. Bookstore is **not a git repo** (loss risk).

## Status & next
Working prototype skeleton. Consider `git init` on Bookstore.

## Related
- Personal commerce; distinct from the DH portfolio.
