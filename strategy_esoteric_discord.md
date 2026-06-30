---
title: "Strategy — The Esoteric Studies Discord (Commons)"
type: strategy
category: synthesis
description: "Design for an esoteric-studies scholarly Discord, modeled on the Vibe Coding Garage; channels, roles, bots, governance, SocMag integration."
tags: [strategy, discord, community, socmag, outreach, vibe-coding-garage]
---

# The Esoteric Studies Discord (the Commons)

> Companion to [[strategy_esoteric_platform]]. Modeled on the **Vibe Coding Garage**
> ([[project_vibecoding]]) — the proven testbed for piping a solitary DH practice into a
> live, multiplayer space — and on the "Social Megaphone" pattern
> ([[concept_database_theories]]).

## 1. What it is, and what it is *not*
**Is:** the *commons* layer of the platform — the place the thousands who watch the
videos and read the portals can actually *talk*, ask, share finds, study together, and
(for some) find their way into SocMag. A warm middle between a YouTube comment section
and an academic listserv.

**Is not:** a replacement for SocMag's members-only governance, the journal, or
peer review. It's the *front porch*, not the boardroom. Keep the society's private
business on the society's private site.

**Lesson carried from VCG:** a Discord generates enormous transcript value (your
SocialsDB/Megabase precedent). Design from day one to **mine it ethically** — the best
threads become newsletter items, reading lists, and "what's new" posts.

## 2. Roles (kept few — role sprawl kills communities)
- **@Member** — anyone who joins (after onboarding). Read/post in commons.
- **@SocMag Member** — *verified* against a SocMag account (the on-ramp payoff). Gets a
  members' lounge + a visible badge. This is the funnel's reward and SocMag's growth lever.
- **@Scholar** — self-identified faculty/grad/independent researcher; light verification
  (a homepage/ORCID/affiliation). Can host AMAs / reading groups.
- **@Steward** — the 2–3 co-moderators you recruit (sustainability is non-negotiable).
- **@Creator** — partner podcasters/YouTubers you index (SHWEP, Esoterica, etc.); a
  channel to share new drops. Turns the feed relationship into a personal one.
- **@Bot** — the automation.

Tiered, not hierarchical: most people are just @Member. Verification is an *invitation*,
not a gate to basic participation.

## 3. Channel map (start SMALL — ~10 channels, grow on demand)
**▸ WELCOME**
- `#start-here` — rules, the fan-index ethics ("link & credit, support creators"),
  the academic↔practitioner norm, how to verify as a SocMag member.
- `#introductions` — name, interests, what brought you.

**▸ THE FEED** (ties to EsotericBeatNews)
- `#new-episodes` — **bot-posted**: every new episode from the EsotericBeatNews catalog,
  auto-tagged. The always-fresh heartbeat; zero manual effort.
- `#whats-new` — human-curated highlights, conferences, CFPs, publications, jobs.

**▸ THE LIBRARY** (ties to the knowledge portals)
- `#reading-room` — discuss primary sources & the portal sites (Atalanta, grimoires,
  Crowley, witchcraft studies…); link to the relevant DB pages.
- `#ask-a-question` — "where do I start with X?" The single most valuable channel for
  outreach; converts lurkers to participants.
- `#reading-groups` — scheduled slow-reads (a SHWEP series, a grimoire, a monograph),
  hosted by @Scholar/@Steward.

**▸ THE WORKSHOP** (ties to your tools/games + the VCG DNA)
- `#dh-lab` — the vibe-coding/DH-building channel: people making esoteric DH tools,
  datasets, image pipelines, games. *This is the VCG, reborn with a scholarly subject.*
- `#show-and-tell` — share projects, visualizations, EmblemPrintShop finds, sigil CV runs.

**▸ THE COMMONS**
- `#general`, `#off-topic`, `#voice` (for reading-group calls / casual hangs).

**▸ SOCMAG** (gated to @SocMag Member)
- `#members-lounge` — the verified-scholar space; light society chatter, not governance.

## 4. Bots (lean on your existing pipelines; don't buy bloat)
1. **Feed bot (build this; it's the keystone).** A tiny scheduled job reads the
   EsotericBeatNews `catalog.json` (you already produce it), diffs against last-seen, and
   posts new episodes to `#new-episodes` via a Discord webhook. **No bot framework
   needed — a webhook + your existing build pipeline.** This single automation makes the
   server feel alive with ~zero ongoing labor.
2. **Verify bot.** Ties a Discord user to a SocMag account (a one-time code emailed via
   the society site once the email provider is on, or a manual @Steward grant at first).
   Grants @SocMag Member. *This is the literal outreach mechanism.*
3. **Digest bot (later, the Megaphone payoff).** Weekly, summarizes the best threads +
   new episodes into a draft "what's new in esoteric studies" post for the SocMag
   newsletter/socials — human-reviewed before publishing. Reuses your Social-Megaphone
   extraction pattern; turns community chatter into outreach content automatically.
4. Off-the-shelf for the boring parts (mod logs, roles-on-react): a standard bot
   (Carl-bot/MEE6). Don't custom-build what's commodity.

## 5. Onboarding (the conversion path)
1. Land in `#start-here` → react to accept norms → unlock the server.
2. `#introductions` prompt nudges interests (feeds future reading-group matching).
3. A pinned, friendly ladder: *watch the feed → ask in `#ask-a-question` → join a
   reading group → verify as a SocMag member → consider membership/the journal.*
4. The **only** push toward SocMag is the verified badge + members-lounge — pull, not
   shove. Outreach that feels like a sales funnel will repel this audience.

## 6. Governance & safety (do this before you invite anyone)
- **Recruit 2–3 @Stewards first.** A solo-modded server is a burnout/abandonment risk —
  the exact failure the platform doc warns about.
- **Clear, short rules:** scholarly generosity; cite/credit; support creators; the
  academic↔practitioner norm ("history-of vs. practice-of" both welcome, sneering at
  neither); standard anti-harassment.
- **Esoteric-specific care:** the field draws sincere practitioners *and* edgelords/
  conspiracy drift. State plainly: this is a space for *study*; no medical/legal/financial
  "magic" advice, no hate dressed as tradition. Stewards enforce early and visibly.
- **Privacy:** if you mine transcripts (you will, per VCG precedent), say so in the
  rules, anonymize in any public output, and never surface DMs. Your SocMag privacy
  instincts ([[concept_database_theories]], and the SocMag per-field consent model) apply
  here too.
- **Data/back-of-house:** keep a periodic export; don't let the community's memory live
  only inside Discord.

## 7. Seeding & launch (avoid the empty-room death)
1. **Soft-launch from VCG + your network** — invite the people already in your orbit; a
   server with 15 talking people beats 500 silent ones.
2. **Pre-fill the feed** — the feed bot back-posting a week of episodes makes it look
   alive on day one.
3. **Anchor events** — schedule the first reading group + one @Creator AMA before the
   public invite. People join for *something happening*, not for a channel list.
4. **Then** announce via EsotericBeatNews, SocMag's channels, and partner creators.

## 8. How it ties back to the platform
- The **feed** fills `#new-episodes` (discovery → conversation).
- The **portals** anchor `#reading-room` / `#reading-groups` (conversation → depth).
- The **workshop/tools** live in `#dh-lab` (the VCG spirit, now subject-driven).
- **SocMag** is the verified lounge + the funnel's destination (commons → society).
- The **Megaphone digest** turns all of it back into SocMag outreach content.

One front porch for the whole house. Start with ~10 channels, three stewards, one feed
bot, and a reading group — and let demand, not ambition, grow it.
