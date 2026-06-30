---
title: "Funnels — explained at three levels"
type: concept
category: explainer
description: "What a funnel is, explained for a 15-year-old, a college student, and a grad student. Grounded in the esoteric-studies platform."
tags: [funnel, outreach, community, metrics, explainer]
---

# Funnels, at three altitudes

A companion to [[strategy_esoteric_platform]] and [[strategy_esoteric_discord]], where
"the funnel" does a lot of work. Here's the same idea three ways — each level assumes
more and hedges less.

---

## 🧒 Like you're 15

A **funnel** is that cone-shaped thing you pour stuff into — wide at the top, skinny at
the bottom. People use the word "funnel" for how a crowd of people slowly shrinks down to
a few people who really care.

Picture your YouTube channel about magic history.

- **A LOT** of people see a video. (Top — super wide.)
- **Fewer** of them actually click and watch the whole thing.
- **Fewer still** go "huh, I want more of this" and join your Discord.
- And **only a few** of those become real members of the Society, pay dues, show up to
  stuff.

Each step, you lose some people. That's normal — *it's supposed to get narrower.* Nobody
goes from "saw a video once" straight to "card-carrying member" in one jump. The funnel
is just the path: stranger → fan → regular → member.

Two things this teaches you:
1. **You need a big top.** If only 10 people ever hear about you, the bottom is basically
   zero. Get seen by lots of people first.
2. **Don't skip steps.** You can't ask a total stranger to join a society. You walk them
   down: first give them something free and cool (videos, a feed), *then* a place to hang
   out (Discord), *then* invite them deeper (membership).

That's it. A funnel = the journey from "never heard of you" to "all in," and the fact
that the crowd shrinks at every step.

---

## 🎓 Like you're a college student

A **funnel** (a "conversion funnel" or "marketing funnel") is a model of how strangers
become committed participants, broken into **stages**, where you lose a fraction of
people at each stage. It's a way to *think in steps and measure them*.

A classic version (the AIDA model) has stages like:

| Stage | Esoteric-studies platform example | What you measure |
|---|---|---|
| **Awareness** | Someone sees an Esoterica/SHWEP video, finds EsotericBeatNews | reach, impressions, unique visitors |
| **Interest** | They browse the feed, read a portal page, watch more | time on site, pages/visit, return visits |
| **Consideration** | They join the Discord, lurk, ask a question | Discord joins, % who post |
| **Conversion** | They verify as / become a SocMag member, pay dues | signups, paid members |
| **Retention / Advocacy** | They renew, post regularly, bring friends | renewal rate, referrals |

The key concept is the **conversion rate** between stages: of everyone at stage N, what
fraction reaches stage N+1? Say 100,000 people watch the videos, 5,000 visit the feed,
500 join the Discord, 50 become members. Your stage conversions are 5% → 10% → 10%.

This reframes growth as a set of **leaks to plug**. Two levers:
1. **Widen the top** (more awareness) — every downstream number scales with it.
2. **Improve a conversion rate** (a "leaky" step) — sometimes the cheapest win. If only
   1% of feed-visitors join the Discord, a clearer "join the conversation" button might
   double it without a single new viewer.

You also learn to spot the **biggest leak**. If 100k watch but only 5k hit the feed,
your problem isn't membership — it's that nobody's making the jump from YouTube to your
site. Fix the *worst* step, not the last step.

Caveats a college course would add:
- **Funnels are leaky on purpose**, but a *too-narrow* step early on starves everything
  after it.
- **Different content for different stages.** Top-of-funnel = broad and free (the feed).
  Bottom = specific and committed (the journal, conferences). Don't pitch membership to
  someone who just arrived.
- **It's a model, not reality.** People don't actually march straight down; they wander.
  But the model is useful for deciding *where to spend effort.*

---

## 🧑‍🔬 Like you're a grad student

The funnel is a **descriptive heuristic that hardened into a normative one**, and the
interesting work is in knowing when the abstraction earns its keep and when it distorts
the thing you actually care about.

**1. The funnel is a lossy linearization of a non-linear process.** The cone implies a
monotonic, one-way descent through discrete stages. Real participation is a *graph*, not
a pipeline: people loop, lapse and return, enter "mid-funnel" (a colleague drags a
scholar straight into the Discord), advocate before they convert, or convert without ever
"considering." The funnel survives as a tool because it's *legible and actionable*, not
because it's faithful. Treat it as a coordinate system for allocating attention, not a
theory of behavior.

**2. Successor models exist; choose deliberately.**
- **AARRR / "pirate metrics"** (Acquisition, Activation, Retention, Referral, Revenue)
  foregrounds *retention* and *referral* — the loops the classic funnel omits.
- **The flywheel** (Brian Halligan / community-led growth) inverts the funnel: satisfied
  participants *become* the acquisition channel, so the bottom feeds the top. For a
  **commons**, this is the truer model — a scholarly community grows by members bringing
  members, not by a marketing department pouring strangers in the top.
- **Jobs-to-be-done / journey mapping** drops the aggregate cone for the individual's
  motivating "job" ("I need a credible entry point to Renaissance magic"), which is often
  more generative for *what to build* than for *what to measure*.

**3. Measurement validity and Goodhart's law.** Each funnel stage requires an operational
proxy (a "member" = a paid `bf_dues_invoice`; "engaged" = posted in Discord). The proxy
is never the construct. Once you optimize a metric it ceases to measure what it did —
maximize "Discord joins" and you get a dead server of 5,000 lurkers; maximize "signups"
with a fake-throwaway and you corrupt the roster (cf. the SocMag e2e test that
*deliberately* created and deleted a junk account). Define stages by **leading indicators
of genuine value**, and pair every count with a quality/health metric.

**4. The economics the cone hides.** Funnel optimization is really an argument about
**CAC vs. LTV** (cost to acquire vs. lifetime value) and about **cohort behavior over
time**. Aggregate conversion rates are Simpson's-paradox traps: a blended 10% can hide a
40%-converting cohort (scholars arriving via SHWEP) and a 1% cohort (random virality).
**Cohort and channel segmentation** is where the real insight lives — *which source
produces members who renew*, not which produces the most clicks. A small, high-intent
top-of-funnel often beats a large, low-intent one.

**5. Selection effects and the denominator problem.** "Conversion rate" is hostage to who
entered. Broaden acquisition and your rates *fall* even as absolute outcomes rise (you
added low-intent people to the denominator) — so a falling conversion rate can be a sign
of success, not failure. Never read a ratio without its base.

**6. The normative critique — funnels and the commons.** Funnel-thinking imports a
*commercial telos*: every interaction is instrumentalized toward a terminal conversion
(the sale; the dues payment). Applied uncritically to a **scholarly community**, this
corrodes the very thing that gives the community value — its non-instrumental,
gift-economy character. A reader in `#ask-a-question` who never "converts" is not a leak;
they may be the field's future, or simply a person the commons exists to serve. The
ethical move is to treat the funnel as **one lens among several** — useful for deciding
where SocMag spends scarce outreach effort — while refusing to let "conversion" become
the definition of a participant's worth. The flywheel framing helps here: it makes
*serving people well* and *growing* the same act, rather than opposed ones.

**7. Practical synthesis for the platform.** Use the funnel **descriptively** to find the
single worst leak (almost certainly YouTube-audience → owned-property, the
feed/Discord), instrument it with honest proxies + a quality counter, segment by source
cohort to learn *which* relationships (SHWEP, Esoterica) actually yield renewing members,
and then **switch mental models to the flywheel** for the part you actually want to be
true: a commons whose members, well served, recruit the next ones. The funnel tells you
where to push; the flywheel tells you what to build.

> TL;DR across the levels: a funnel is *the crowd shrinking as it commits* (15); *a staged
> model with measurable conversion rates and leaks to plug* (college); *a lossy,
> instrumentalizing linearization best used as one diagnostic lens — paired with cohort
> economics and a flywheel ethic — lest you optimize a proxy and corrode the commons*
> (grad).
