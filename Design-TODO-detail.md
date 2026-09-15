# Design To-Do — Detail (Claude's copy)

Companion to `Design-TODO.md`. The short list is Yuehui's, written in her voice and deliberately
terse. This file holds the expansion: what each line actually means, where it came from, open
questions, and which files in this folder are relevant. When Yuehui asks "what did I mean by X",
answer from here.

**Rules for maintaining this pair:**

1. `Design-TODO.md` is the source of truth for *what's open*. Never pad it with description.
   One line per task, her phrasing, `->` for the "and then" clause, date tag `(M/D)` for the meeting.
2. This file mirrors the same section order. Each entry keys off the short line verbatim so the
   two can be matched by eye.
3. When a new meeting's tasks arrive (pasted notes, or extracted from Otter.ai), add terse lines
   to the short list first, then expand here. Don't reorder her existing sections.
4. When something is finished, move the line to **Done** in the short list with a date; move the
   detail entry to the Archive section here rather than deleting it.

---

## Caregiver — Patient App

Source: team meeting Fri **2026-08-07**. This is the priority block right now — messaging is
explicitly *not* Yuehui's blocker (see Provider — Patient).

### "Redesign the care recipient view -> not just allergies / meds / conditions / procedures"

Today the caregiver's view of a care recipient is limited to four clinical lists: allergies,
medications, conditions, procedures. That's a record, not a dashboard — it tells a caregiver what
was documented, not how the person is doing. The redesign target is a view that answers "how is
Mom this week" before it answers "what is Mom's problem list".

### "Add: recent wellness (steps, goals met), labs / vitals + high-level evaluation, ask Orion about their data"

Three additions, in rough priority order:

- **Recent wellness** — steps, goals met, the daily-tracker style signals. Cheap to read, high
  reassurance value, and it's the thing a caregiver checks daily rather than monthly.
- **Labs / vitals + high-level evaluation** — not the raw full-data table. The vitality /
  evaluation summary layer that already exists on the patient and provider side, reused here.
  Cross-ref the vitality evaluation work noted for the Provider Dashboard.
- **Ask Orion about the care recipient's data** — parity with the provider view's Orion. Open
  question for Yuehui to resolve in design: does caregiver-Orion answer in the same voice and with
  the same source-trace / grounding chips as patient-Orion? Existing decisions that apply:
  Orion speaks in first person ("I"), and suggested follow-up chips *fill* the input rather than
  send. Source-chip and grounding work in this folder (`orion-source-chip-spec.html`,
  `orion-grounding-groups-expanded.html`, `orion-peek-summary-copy.html`) is the pattern to inherit.

### "Keep it a minimal caregiver dashboard, still inside the patient app"

Scope guard from the meeting. No separate caregiver app, no new tab structure. It lives in the
existing patient app (4 tabs + center Orion button). "Minimal but meaningful" was the phrase used.

### "Caregiver with multiple family members -> Network tab as the entry point"

The UX model question: a caregiver may manage several people (two kids, a parent, a spouse). The
proposal on the table is that the **Network tab** lists all care recipients and is where you pick
whose data to look at. Worth checking against the existing health network / connections work
(`patient-connections-screen.html`, `connect-combined-flow.html`) so this doesn't invent a second
concept of "people I'm connected to".

### "Nav model: caregiver's own profile -> care recipient -> back"

Define the round trip. How do you get in, how do you know you're in, how do you get out. The
"how do you know you're in" half is the separate line about always showing whose data is on screen.

### "Quick view vs. log in as that user -> define the UX expectation, engineering decides the tech"

Concept-level only. Two distinct experiences to name and bound:

- **Quick view** — read the care recipient's information without impersonating their account.
  Probably the default for the caregiver dashboard.
- **Full login-as** — actually operating as that user. Needed for some actions (logging a dose for
  a child?), but heavier and riskier.

Yuehui's job is to say when each is appropriate and what the user should expect; engineering picks
the technical approach. Two design constraints stated in the meeting: keep it simple for a parent
managing children and for an adult child managing an older parent, and make it unambiguous in the
UI whose data is currently being viewed.

### "Always show whose data is on screen"

Persistent, not a one-time confirmation. This is the safety rail for the whole caregiver model —
a caregiver logging a med against the wrong person is the failure mode to design out.

### "Future caregiver-specific app / dashboard -> note the idea, don't design it now"

Explicitly parked in the meeting. Capture the thinking so it isn't lost, but current focus stays on
the in-patient-app caregiver view.

### "Leave room for messaging -> where the caregiver would see threads with provider / patient later"

Anticipatory only. Don't design the messaging UI; just don't build a caregiver layout that has
nowhere to put a thread list later.


### Added from the caregiver design review, Mon 2026-08-25

Attendees: Yuehui, Kelly, Jayanth. Yuehui walked the caregiver framework; most of the block below is
feedback on that walkthrough. Deadline attached to nearly all of it: **Greg sees this next Tuesday**.

#### "Finish the pop-ups and the screen content -> the framework is already there"

Her own words in the meeting: *"it's still like work in progress… a lot of I think little pop-ups,
the screen content I need to figure out, but the framework is already there."* The skeleton — network
screen, connected-person dashboard, access management — is settled. What's missing is the content
layer.

#### "Connect People grouping -> highlight group is the people who share with me, separate section for the people I share with"

The grouping she brought in was (a) people you share with in either direction, (b) "connected only".
Kelly rejected the mixed group. **Decision: the primary group is the people whose data I can see**,
because that's why you come to this screen — Kelly: *"the primary function of coming to this screen
is that I want to go look at dad's something or another… when's Dad's appointment… did Dad get a good
night's sleep?"*

Yuehui's objection stands and is why the sub-tasks exist: most real relationships are bidirectional.
*"it cannot clearly just lead two groups… most of time probably is mixed together."*

- **Icon or colour code for both-ways.** Kelly's fix rather than a third group: *"maybe there's a
  little icon or color code that indicates they also can see you, and then there's a section for
  shared with."*
- **"Connected only" is dead.** Jayanth twice said he couldn't find a use case. Yuehui's case was
  keeping Dad in the network after both sides revoked. Kelly reframed it: *"maybe there's a
  deactivated section instead of connected only, so it shows that you can reactivate it versus
  you've deleted them completely from your network."* Yuehui's framing to preserve: *"between sharing
  data and remove from a list, there's some middle point in between."*
- **Default count.** Four is a placeholder. Open: slider vs. list once there are more than four.

Mental model referenced throughout: a social-media friends list.

#### "Source tiles -> we don't get logos from the health systems, today it's the letter avatar"

She wanted compact preview rows with a logo per source. Jayanth confirmed the gap: *"The app has the
logo… We don't get the logo."* Today the app falls back to the initial letter as the avatar. Open
design problem: keep the row compact and still identifiable without a brand mark.

#### "Show health systems the same way as people -> Jay says they get revisited often"

Her assumption was that sources are set-and-forget. Jayanth pushed back: *"they will probably check
the health systems frequently… maybe want to think about showing the health systems the same way
you're showing the people."* This is a structural change to the network screen, not a styling note.

#### "Connected person dashboard -> decide whether their connected sources show at all"

Her explicit product question, still open: *"can caregiver see or even edit research connect sources?
Like, if not, probably we don't need to show this section."* It resolves into the act-as-me scope —
if a caregiver can't manage Dad's connections, the section is dead weight.

The dashboard as presented: visit essentials · add data · access management · notification placeholder
· vitality board · Orion summary · a flexible grid of small cards (meds today, sleep / activity /
nutrition coming) · Health Hub with upcoming appointments, active conditions, active meds and
allergies, everything else clubbed into "more records".

#### "Action-oriented view -> what does Dad need to do today and how do I help"

Kelly's reframe of the whole dashboard, and the most consequential open note in the block:
*"if I'm Dad's caregiver, my priority is probably not reviewing all of his stuff. It's I want a
summary of what actions are needed, what his treatment plan is, what the schedules, the appointments,
what conditions he needs monitored… rather than just access, it's really more of what does Dad need
to do, and how do I help him make that happen? So maybe we can brainstorm about what those actions
are and put that in the story too."*

Yuehui's related distinction: visit essentials is a *before the visit* surface; the dashboard should
be a *daily* surface. *"did your dad feel good, all good today, or is there any actions need to do
today or recently?"*

Deferred to later: stats on who viewed your account and how often. Today you can see what you share,
not the frequency it's read.

#### "Health Hub category detail list -> better looking item / field card"

Her own open item. *"for the items color field card, I'm thinking about is there any better looking
way to do that… I don't think that will require a lot of effort."* Small, cheap, self-assigned.

#### "Show Greg the caregiver UI and flows next Tuesday"

Confirmed twice. She deliberately did **not** show it in the 8/25 team meeting — Kelly: *"you're not
going to show the Caregiver's stuff today to Greg, you want some time to update, and then we'll plan
on showing him more details next week."* Kelly told Greg the caregiver work is ready for review and
that a treatment-plan first pass lands the same day. Greg's sign-off is what unblocks dev.

### Added from the design review Mon 2026-08-31 + the Greg walkthrough Tue 2026-09-01

#### "Practitioner list is cluttered with nurses"

Greg's own hospital stay, 9/1 at 0:10:00: *"when I went to the hospital, I had a doctor, but then it's
showing 20 other people that were involved that were nurses, and it just makes it untenable to figure
out who's who."* His instinct: *"we should only capture the doctors, not all the nurses."*

Kelly's correction, which is the design you have to make legible: the app already separates the two.
Health systems lists primary care only; All practitioners lists everyone the connection returned. Greg
was not seeing that separation. *"Correct, but we separate that in the portfolio."* Her suggested fix,
which Greg accepted: *"maybe at the top there's just a filter for all practitioners versus primary
care."*

Your answer in the room was that the care team currently supplies this and you are open to regrouping.
So the task is not to drop nurses, it is to make the existing split visible at a glance.

#### "'Last update' with the date instead of a status"

From 8/31. Replace the status wording on caregiver connection cards with "Last update" plus the date.
Show red **only** when an appointment happened after the last refresh, meaning there is data you do not
have yet. Gray otherwise. Two statuses, not a spectrum.

#### "Restore the 'whose records am I viewing' banner"

Also 8/31, and it is a regression rather than a new idea: the persistent whose-data banner from the
earlier caregiver work went missing in the redesign. Restore it and pair it with an explicit exit or
back-to-my-account control. This is the safety rail for the whole caregiver model, so it should not be
the thing that gets dropped when the layout gets tight.

You did demo the banner to Greg on 9/1 (*"there were always the banner here, like you are in someone
else's health records"*), so check whether the gap is only in some frames.

---

## Caregiver — Access & Sharing

Source: caregiver design review **2026-08-25**. Split out from the caregiver dashboard because it's a
separate surface with its own permission model, its own premium gating, and its own consent problem.

### "Two grants, two buttons -> view only, and act as me"

Kelly's structure: *"there's like a separate button. So give them access to all this and another
button that says they can act on my behalf in my account."* Two named modes — **view only** and
**act as me** (also called full access).

What act-as-me covers, per Kelly: *"They can connect health systems. They can add medications or
supplements, they can add, upload data. They can schedule appointments if that's a feature."*

- **v1 is UI only, no Orion.** Jayanth: *"the simpler part would be is to just give them the UI and
  not access Orion… they can do the refresh connection, but it's only through UI, not through
  Orion."* The blocker Yuehui named: add-meds runs through Orion today, so that action can't be in
  the first phase.
- **Premium on both sides.** Both the caregiver and the person being cared for must be premium —
  Kelly: *"they both have to have a premium to do the act as me at whichever way it goes."* Design
  consequence Yuehui already flagged: when the counterpart is base, the feature shows blocked /
  inactive with a premium mark. A **family plan** (Kelly floated ~$9.99/mo for three) is being taken
  to Greg — pricing isn't hers to settle, but the upgrade prompt is.
- **Pick the shippable slice.** Kelly: *"whatever the initial phase or second phase is that says,
  well, if you're acting as someone, here's the one to three things that from a dev standpoint we
  could make happen, and then we could always expand it from there."*

Base-vs-premium content rules stated by Jayanth, one of them contested: no Orion insights, no
summaries, no treatment plan for base. Kelly pushed back on past-visit summary being excluded and it
was left unresolved. Without act-as-me, a caregiver can only change the status of conditions and meds,
and log meds.

### "Locked categories -> the receiver can only request more, never less"

The control rule, from Jayanth: *"whoever is sharing should have the capital D to share… B should not
even have access to share."* Yuehui's UI expression of it: *"dad grant the conditions, meds and
allergy to me, so I cannot uncheck them. This is locked. I can only request more."*

"Show less to me" was considered and dropped — Kelly saw no reason to refuse data.

- **Templated request note, not free text.** Kelly: *"It's a templated note, not a note that they can
  put in… if users say I want to add a note, we could talk about it later."*
- **Request tracker with withdraw.** Already designed: *"your request is sent on specific date, and
  you can choose to withdraw."*
- **Granted state on the row.** Kelly wants it legible: *"granted access — act as, or view only — as
  of certain date."*

No expiry in v1. Access is permanent until revoked; the QR code and the PDF remain the one-time
snapshot mechanisms.

Two management entry points, both designed: *"the data I receive from my dad"* (locked categories,
request more) and *"manage the data I share with my dad"* (applies immediately, no approval loop —
grant more, switch view-only to act-as-me, grant fewer, or stop entirely).

### "Build the sharer's screen for an incoming request -> that's the screen I'm missing"

Verbatim gap she called out: *"I didn't have the dad's screen. That's the screen I'm missing."* The
request flow is designed from the requester's side only. What Dad sees when a request arrives —
notification, review, grant or decline — doesn't exist yet.

### "Mode indicator -> pop-up when a view-only user hits add / edit, persistent banner in act-as-me"

Two treatments:

- **View only** hitting an edit or add action gets a pop-up ("view only, cannot add any records") with
  a path to request act-as-me from the sharer.
- **Act as me** gets a small persistent banner on every screen — Orion, manual add records, add meds,
  data cleansing, Vitality, meds / supplement goal logging. On the connected person's Vitality screen
  the banner carries no exit button: *"it's meaningless to have the access button, so it just
  indicates that you're in your dad's health records right now."*

This is the 8/7 "always show whose data is on screen" line, now with a concrete pattern.

### "Define when the caregiver can exit caregiver mode and when they can't"

Open, and dependent on Jay. Her working hypothesis: no exit from data cleansing (you're mid-flow in
Dad's records), but yes from the Orion chat, switching cleanly back to your own profile. *"I'm not
sure from Jay your backend how easy or how hard it is."* Related behaviour already designed: opening
Orion from caregiver mode switches back to your own profile and shows a toast saying so.

### "Orion's perspective in caregiver mode -> 'his meds' not 'your meds'"

Parked. Her framing: *"if you are in your dad's health records but Orion says your meds are staying
on track, it doesn't make any sense."* Jayanth thought the banner might carry enough context.
Agreed to revisit — *"let's think about the first priority."*

### "Share my health data selector -> subtitle under every category, no hover on mobile"

The problem Kelly stated: *"right now I can't say don't show Dad I take lithium. It would be
medications all or none, right? Mental health, substance abuse… We just need a way to give a
disclaimer of sorts, like this includes sensitive data."* Sharing is per category, all-or-none within
a category — there is no item-level suppression, and there won't be in v1.

Yuehui's resolved strategy: *"my strategy will be the subtitle, and maybe highlight with some icon
like this one might include some sensitive information."* Hover was ruled out — *"on the mobile you
cannot have hovers."*

- **Sensitive-information icon** on the categories that can contain mental health, substance abuse,
  STD history.
- **Default everything on + Select All.** Kelly, relaying Dr. Portu: *"we want to default all of them
  on and get a select all button."*
- **Disclaimer at the top or bottom** of the Share my health data screen: it alerts the user that
  they're sharing everything inside the selected category, sensitive content included.

Note the asymmetry: for **act as me**, every category is checked by default and can't be de-selected,
because add-records writes across all categories. That's a stated system limitation to surface, not
hide.

### "Research the consent wording -> what do EMR patient portals use when you add a caregiver"

Assigned in the meeting, Kelly offering help. Her framing: *"it's not really a HIPAA thing, right?
Because we're not a covered entity. But I wonder what — maybe we can look into what the EMRs, the
patient portals, do when you add a caregiver to that portal. What kind of disclaimer do they use?"*
And: *"there's got to be something the patient is clearly consenting to to give their son or caregiver
full access to all of their health data."* Deliverable is wording, shared back with the team.

### "Notification design -> every change / daily summary / weekly summary, and per-person on-off"

Her concept, to be brought to the finalized version. Three grains of "tell me when the caregiver does
something", plus Kelly's addition that the receiver needs per-person on-off too. Two directions to
cover:

- **Sharer → receiver**: Dad shared more information. Kelly wants it in today's to-dos and as a push,
  *"so I don't have to log in to know Dad shared with me."*
- **Caregiver → sharer**: whenever the caregiver adds or edits a record, the account owner is told.

Future, noted not designed: new-data notifications from partner connections (labs are in, Dad has a
new appointment).

### Added from the design review Mon 2026-08-31

#### "Standardize every consent / data-sharing list across provider, patient, network, QR and FHIR"

Kelly's action item from 8/31, and the point is that the same list currently appears in five flows with
five different sets of categories. One canonical list, used everywhere: provider access, patient
sharing, network connections, the QR code flow, and the FHIR consent screen.

Three specific requirements: **include uploaded documents and wellness data** (Kelly, 0:28:44: *"if
wellness data is already included in vitality and goals, that's fine, but we need to be specific that
the user is consenting and the provider is requesting wellness data"*), provide **Select All**, and
**default every category to on**.

Note this overlaps the existing "Default everything on + a Select All button" sub-line under the share
selector. Same rule, wider scope: it is now every consent surface, not just that one screen.

#### "HL7 / FHIR observation categories to our user-facing categories"

Your action item from 8/31: build the crosswalk from HL7 / FHIR observation categories to the
user-facing health data categories, and share it with Kelly and Jay. The related work already in the
folder is the LOINC category mapping (7 real categories, and the 20 defects logged against the source
file), so start from that rather than from the spec.
### 9/4 additions — team meeting Fri **2026-09-04** ("Discuss open items", 1h30m)

### "Jay's interim permissions rework is a placeholder for my sharing / caregiver design"

Jayanth shipped a permissions restructure to stage on 9/4 and labelled it a stand-in for Yuehui's
work twice, unprompted: *"This kind of ties into what UHe is doing also, but not exactly"* and
*"This all ties into UH updates around sharing and caregiver in the future. But initially I went
with a simpler version for now to prep this for CareCloud users, basically."*

What actually changed, so the caregiver design doesn't re-decide it by accident:

- **"Provider Consent Request" is now "Provider Access"**, and it moved out of Employee Services to
  the top level. Jayanth: *"Provider consent request didn't make sense. We'll obviously change this
  in the future with caregiver with UH update."*
- **A new "Manage Sharing" entry** sits alongside it.
- **Patient + care team permissions are default-on and non-optional**, and the permission list was
  trimmed to only what the provider can actually see.

Treat all of it as provisional. The rename in particular is his placeholder, not a naming decision.

### "Select all / deselect all comes with my caregiver UI update"

Confirms the 8/25 line rather than adding to it. Kelly: *"can we still get a select all button? So
select or deselect all."* Jayanth: *"Yeah, with the caregiver UI updates, I'll bring those in. But
for now, I think I toggled them all on so that we don't have to."* Kelly: *"Good for now."* So the
Select All affordance is formally on Yuehui's side of the line, not his.

### "New patient-facing header 'Used by Orion Answers Only'"

A new grouping header on the patient permission screen covering diagnostic reports, health-system
documents, uploaded documents, care plans and health kits — everything that is reachable only
through Orion, not through the provider dashboard. Jayanth's rationale: *"if you give access to care
plans, it's only through Orion that they can access that information. What can you access through
Orion versus what can provider actually see in the dashboard? That there is also a differentiator
for that."*

This is the same distinction the standardized consent list has to carry (see the 8/31 line). Worth
checking whether "Used by Orion Answers Only" survives as the label or whether the sensitivity /
subtitle pattern already covers it.

### "Practices ask for SMS -> phone notification first"

Daphne, on invites: *"Is there a way to receive it through text message?"* and *"a lot of times,
text is usually the preferred method of communication with patients."* Jayanth: *"Not now, but in
the future, maybe."* Kelly routed it to work already assigned: *"That'll be in our messaging feature
updates… Yuehui is also working on the design for notifications that would come on your phone. So
it's not a direct text, but it's a notification that you have to approve access to your account."*

So: no SMS design now. The push-notification design already on the list is the answer given to
practices, which raises the bar on it — one of its jobs is the access-approval notification.


---

## Data Refresh & Appointments

Source: caregiver design review **2026-08-25**. Kelly explicitly scoped this to both surfaces:
*"if you could in the caregiver as well as you know for the main platform, think about what this auto
refresh will look like for the health systems, because certainly we want it to be seamless for the
user."*

### "Auto-refresh for health systems -> design it for the main app and the caregiver view"

The principle, from Kelly: *"it should be as seamless and easy for them, and not always the person
having to remember to go in and refresh."* Devices and apps already refresh on their own; wellness
data refreshes every time the app opens. Health systems are the hard case.

- **Appointment is the trigger for partner systems.** Jayanth: *"the real deal breaker is if they give
  us appointments or not because if we don't have the appointment data, then we don't know when to
  trigger it… The only thing that would make sense is if they had an appointment with that specific
  health system."* Kelly's worked example: visit yesterday, log in today, refresh fires, lab orders
  land, refresh again.
- **Non-partner systems get a notification instead.** Kelly: *"if they're connected to a system that's
  not a partner, we want to give them a notification to refresh."* Sketched wording: *"hey, how was
  the appointment? Would you like to refresh your data?"* Kelly is writing this as one epic with
  separate stories for the partner-appointment path and the non-partner notification path.
- **Entry point undecided.** Yuehui: *"I'm not sure from the entry points from their health system is
  the best way, or from specific data or something."*

Caregiver propagation is decided: refreshing the sharer's data automatically refreshes whatever the
caregiver has access to. Jayanth's boundary — *"we shouldn't touch their network systems or anything
like that. Not yet. It should just refresh their data."*

Constraint worth knowing: EMR tokens expire in about an hour regardless of the year-long window the
spec allows, so re-login prompts are unavoidable.

### "How do we get the user to enter appointments when the provider isn't a partner"

Kelly put this question directly to Yuehui and then parked it as a later story: *"Yuehui, how do we
encourage the user to enter appointment information or talk about it when it's not a partner
provider."* Widened: *"even if my doctor is the partner, I'm still gonna go see other specialists or
therapists or labs… How are we going to one encourage those connections and then two encourage those
refreshes? Like, maybe first encourage the awareness of those appointments and then connection and
refreshes."*

Adjacent epic Jayanth named but nobody owns yet: scheduling appointments in-app, reading the user's
calendar, writing to Apple Calendar.

### "Appointment adherence as a Care / prevention element"

Yuehui raised it, Kelly took it enthusiastically: *"Absolutely, it's part of prevention, right? Did
you get your annual on time? Did you get your mammogram? Did you get your Pap smear? Did you get your
colonoscopy, flu shot, all that? Absolutely, Yuehui, should be in care."* It also flows to the
provider side as part of the visit-essentials snapshot. Cross-ref the treatment plan block.
### 9/4 additions — team meeting Fri **2026-09-04**

### "Bulk invites without an appointments API"

The invite UI has three tabs — upcoming visits, next-two-days visits, and patient search — and the
first two only work where the EMR exposes appointments. The pilot EMR doesn't. Jayanth: *"this
upcoming visits and two days visits only works if we have an appointments API. Also, unfortunately,
CareCloud doesn't have it, so for them we'll have to figure out some other way to do bulk invites."*
On the fallback tab: *"that's why we have this third tab, which is the worst case scenario… Then
they can still search for their patients, which is not great. But that's the only thing I, for now,
I could think of. But we'll see if there is any way they could upload a list of invites."*

An unsolved design problem stated as an engineering one. Options on the table: a list upload, or a
better search-and-batch flow. Batch cap today is roughly 20-25 patients.

### "Kelly wants a quick daily send in the morning"

Kelly: *"is there something they could do daily in the morning that's a quick, you know, link
send?"* and the reason it matters: *"I think that'll be a big dissatisfier if they've got to do that
one at a time."* Front-desk staff, start of day, no appointment feed to work from — that's the
scenario to design against.

### "Invite email says 'your healthcare provider'"

Small copy fix Jayanth flagged against himself: *"Your healthcare provider. I guess we'll have to
change this to actually include the provider name."* A patient who gets an invite from a nameless
"healthcare provider" has no reason to trust it.


---

## Health Bio & Stats

Source: team weekly **2026-08-25**, the first fifteen minutes. Greg drove it; Kelly noted it was
always in the original story and got lost.

### "Create an abnormal / out-of-range group in stats"

Stats today groups labs into clinical categories (blood, kidney, etc.). Anything not in a category
doesn't trend, so a bad value can sit on the diagnostic report and never surface where the user
actually looks. Greg's version of the failure: *"you naturally look at the stats and you think oh I'm
healthy. You come to the report and you say shit I had two things wrong with me I didn't catch."*

The rule he landed on: *"the stat should include whatever categories you want plus anything that's
out of line."* Kelly confirmed it was in the original story: *"one of them grouped for convenience in
the most common labs, but anything outside normal range was also supposed to be highlighted."*
Yuehui's answer in the meeting was a commitment: *"definitely. I'll create a new group."* Jayanth:
*"we can include out of range. That's a straightforward change. I can probably get that in quickly."*

- **Duplicates are the known problem.** Kelly: *"we had talked about having a category at the top; it
  became kind of challenging because there would be duplicates in the sections."* An out-of-range
  potassium belongs to kidney *and* to the new group. Decide whether it appears twice, is pulled out
  of its category, or is cross-linked.
- **Projections run on the out-of-range items too.** This is the point of putting them in stats rather
  than leaving them on the report — Greg: *"You're going to track it against the next report and want
  to create a projection on it anyway."*
- **Link stats and the diagnostic report.** Kelly's instruction, aimed at Yuehui: *"I think we might
  need to include it instead because that's where all the trends are. So just think about that a
  little bit from your UI perspective, because if it's on here, I may miss it if I'm looking in
  stats, or there's a link or something connecting them."*

### "Health Hub as the other home for the abnormal data"

Yuehui's suggestion in the meeting: *"maybe health hub actually. So that's a place like a kind of like
a dashboard of their health hub. So that's a place we can put the abnormal data."* Stats is where the
trends live; Health Hub is where a summary of "things to look at" belongs. Both, not either.

### "Also flag the values trending the wrong way while still in range"

From the caregiver review, not the weekly, but it's the same mechanism. Kelly, to Yuehui: *"it's not
just things that are outside a normal range. It's also alerting to trends that may be headed in the
wrong direction. So he mentions glucose a lot… if my glucose is heading in the high range, even
though it's still in the normal range."* This is where stats hands off to the plan — a wrong-direction
trend becomes a prevention action.
### 9/4 addition — team meeting Fri **2026-09-04**

### "Fasting vs. non-fasting glucose gets misclassified so the trend splits"

Kelly hit this on her own record: *"I have a glucose trend of only two docs for non-fasting… So I
don't get to see the trend. It's just really it's annoying as a user."* Her read on severity: *"it's
a pretty big deal because it's such a common measurement, and it's also important for diabetes
pre-diabetes determination."* The results are being classified non-fasting when they were fasting,
so one measurement lands as two thin trends.

Jayanth's possible fix is a user-facing one, which is why it may land as design: *"What you're
saying is maybe we update the cleansing to allow the user to change fasting versus not fasting. But
that's just so specific. But I guess we can."* Kelly: *"if you think it is a one-off, we could go
ahead and allow for user change… but I think we need to do something on that."*

**Blocked on Kelly**, who took the action to check the codes and whether it's systemic before anyone
designs an edit affordance. If it becomes one, it belongs with the existing data-cleansing edit
patterns (`data-cleansing-bulk-edit-flow.html`, `tap-to-edit-flow.html`), not a new mechanism.


---

## Reports

Source: team weekly **2026-08-25**. The short line is Yuehui's own note: *check Jay's add-on for the
Reports.* What Jay has built and what Greg wants next are two different things — the check comes
first.

### "Check Jay's add-on for Reports -> see what's actually live before designing on top of it"

- **Diagnostic reports already carry the full panel.** Jayanth, demoing the lipid panel: *"this comes
  across as a report from EMR. But if you scroll down, it shows all of your lab results associated to
  that specific report: triglycerides, cholesterol. Even the ones that don't show in stats show up
  here."* That's the fact underneath the abnormal-group work — the data exists, the surfacing doesn't.
- **The reports tab is being hidden in the provider UI.** Kelly, going through the priority list:
  *"this one's done with the provider UI, so I can hide that reports tab. Jay's got the initial one
  done, so I can hide that."* Confirm what "done and hidden" means before designing against it, and
  what it implies for the patient-side reports surface.

### "Radiology report is a quick fix and ugly -> needs a design pass"

Greg's words: *"We added the radiology report, but it was a quick fix, ugly report. Are we doing
anything around that?"* It's on the list as a design problem with no owner named — take it.

### "Anatomy visual -> Orion generates a picture of what the radiology report describes"

The most concrete new idea in the weekly. Greg's case, from his own injury: *"There's a lot of jargon
that even when you translate it into English, is still jargon because the English is telling you about
anatomy in English words, but the picture is far more interesting because it actually shows me… I
don't know what the fascial tear is and I don't know where it's at."*

Jayanth's implementation shape: *"We can update the reports to show like a visual representation. So
maybe our first stab at doing that image generation thing is with diagnostic reports, and if it has
something to do with imaging, then we generate an image."*

Two follow-ons Greg attached to it, both of which land in the plan rather than the report:

- From the picture, *"you literally can just click — what type of physical therapy can you consider
  based on these anatomy problems?"*
- The existing 3D anatomy widget is on the table for replacement: *"our cute little 3D thing you guys
  did — it's telling me stuff that's useless. It says okay, you got a femur. Well, what does that tell
  me? Whether we keep it or replace it, you guys decide."*

Greg also required the generated image be **saved with the plan** so it doesn't change between plan
revisions: *"you do have to have the ability to save the plan… That way, the image won't change."*
### 9/4 additions — team meeting Fri **2026-09-04**

This is where the 9/4 meeting put most of its weight. The reports item below is the **only formal
action item Otter recorded against Yuehui** for that meeting: *"Review the reports tab and propose a
design for surfacing new and out-of-range lab results, including date handling and an appropriate
category for currently ungrouped data."*

### "Surface new and out-of-range labs on the reports tab"

Kelly's ask, and it started as a personal failure of the product. She got labs from Texas Health
Resources on a Tuesday and the app told her nothing: *"I got my lab's notification from Texas Health
Resources, but I of course didn't get anything in my app, right?… when I went into our app, I knew I
had new labs, and they were kind of there. But the way the stats are categorized, I would have to go
through each category, and there's no color coding or indicator that we designed or talked about in
any story that gives me that here's the new lab."*

Her benchmark is explicit and it isn't flattering: *"if I go into my patient portal — patient portals,
that is one of the very few things they are good at. Get your test results. There it is. There's an
indicator. You've got a new test."* And the target: *"I want to think through the notification so
it's at least as good as the patient portal, hopefully better. That the patients, even though they
don't get a notification, would still prefer to come to C for P rather than their patient portal for
new tests."*

Her own rough proposal, offered as a starting point rather than a spec: *"maybe it's something easy
like a chronological report of here's all your new stuff at the top, and that stays there. I'm
making it up, but if we could put a little design thought to that, Yuhui."* And the principle
underneath it: *"what do we need the user to focus on? Anything abnormal and anything new like that
should be at least the top two."*

**The three-part brief, verbatim** — this is the action item's real content: *"there's probably three
things that are expected on the reports or the to-dos or the homepage or some stats. Out of range,
meaning abnormal, whatever that is, has to be kind of on top or highlighted. But we got to put some
kind of date range to it, right? Because if it's a year old, do we keep showing that? Like that'll be
an important component of it. New, and then the other. So things that aren't currently grouped has to
be in a category of other or somewhere."*

Yuehui accepted it and flagged the obvious risk: *"I want to review the report tab right now because
it's kind of like new to me. I didn't do the design for that, but let me think through that."*
Hence the "review the tab first" clause on the short line.

- **Jayanth first pushed back, then withdrew.** *"can you go into your reports tab, Kelly? That
  should be in chronological order, and it should have your latest lab result on top."* Then: *"I'm
  not saying that there shouldn't be a way where we show new labs. I'm saying I was confused. I
  thought you can't find it anywhere."* So the gap is signalling, not sorting.
- **He deferred the layout outright.** *"That I think is needed. If there is a better way to show it,
  I'm all up for it… maybe show the out of range on top… there might be other ways to show it, Jue."*
- **He is building his own half in parallel.** *"maybe the review your records comes back if there's
  a new lab record that the patient hasn't seen yet… That's a simple enough change for me to add. In
  current review of your records, add observations as a read-only thing."* Trigger: *"On every
  refresh, we show review your records on every refresh."* Design has to assume that exists.
- **No push notification for non-partner systems.** Kelly: *"if we're not partnered with them,
  there's no way we can give them the alert, right?"* So the in-app indicator carries the whole job
  for most patients.
- **The status label is wrong for patients.** Results read *"final"*, straight from the EMR. Jayanth:
  *"the final comes from EMR for diagnostic report. It's not something that we created, but we can
  always map it to something that makes more sense for the patient."* Kelly's point: *"instead of it
  saying final, I knew which tests were normal and abnormal"* in the portal.
- **A report is a collection, not a value.** Jayanth: *"reports is usually a combination of a
  collection of lab results, as in stats, or an actual MRI or imaging study done… if you had your
  blood test, then a diagnostic report comes across as lipid panel with all of your blood results in
  that diagnostic report."* Any "new" or "abnormal" marker has to work at both levels — the report
  and the observations inside it.

**This overlaps the treatment-plan work by Kelly's own framing**, so it may not be a separate
deliverable: *"Yue, for your treatment plan, if you could add this… it would be helpful to make that
kind of the next thing on the reports tab. How do we get lab tests new?"* It is also the same
concept as the 8/25 abnormal-group line under Health Bio & Stats — Kelly grouped them herself: *"I
kind of group these together, so the out of range and the reports, because it's the same concept."*

### "Orion generates the image when an imaging report has no picture"

Greg's ask, relayed by Jayanth, and offered to Yuehui as an experiment rather than a task: *"if you
want to take a crack at it, is if there are images showing images and generating images. I guess we
could use that as the first stab at generating images, especially if it's a knee MRI."*

The case: *"if you click on that, all it has is the text of what that MRI report came back with, and
there is no image, because the EMR didn't give us the image; they only gave us the textual outcome of
that MRI. Then we want to be able to generate that image. Going back to Greg's ask… which might be a
far-fetched idea, but we can try and see."*

Scope constraints he set:

- **Imaging only.** *"only certain ones that are imaging related… if there is a lipid panel report, I
  don't want an image generated for a lipid panel report. But if it is an MRI or an X-ray or a CT
  scan… then we should generate an image if there is no image already as part of the diagnostic
  report."* Open sub-problem he named: how do we detect which reports are imaging-related?
- **Audience.** Yuehui asked: *"it's for user only, right? The provider don't need to see the
  generated image, or it's shared?"* Answer: *"keep it open for both, I would say, but initially for
  the patient, Greg's ask."*
- Yuehui's broader framing, which is the better version of the idea: *"under each report or
  associated to any kinds of data, maybe the user will have the needs to visualize them"* — i.e. the
  documentation / images section per Health Hub category she already proposed on 8/31, not a
  one-off on radiology.

**Paused, and the reason is data, not priority.** There is nothing to design against: Kelly *"we've
had a lot of challenges getting images at all… If I wanted to see my mammogram, I can't do it through
our app, and even when I upload my own, I still don't see it. Like if I ask for it — show me my
latest mammogram — I don't get that. It doesn't pull it up."* Jayanth: *"I think Sutner is the only
one that actually sends images."* Same conclusion as the 8/31 line: image generation needs a job
before it needs a design.

### "Images as their own class in the UI"

Kelly wants imaging separated out: *"what do we need to get you from a coding perspective for images
so that that can be a kind of separate bucket for UI, because it really is a separate class — if it's
an X-ray, a CT, an MRI. And right now those are all under tests or procedures category."* The
concrete failure: *"the issue was when I get a mammogram, it wasn't under the right category to be
clear that that's something I needed to see as an image."*

**Jayanth disagreed**, and his position is the current build: *"I think diagnostic report is the best
place, right? Because diagnostic report should have your mammogram. If you go into your list now, it
should have your previous mammograms there. Whether you have images or not is whether the EMR sent
it or not."*

Kelly parked it herself: *"I'll just keep that on the back burner. But you guys, you're thinking
about it from the image generation — if you have questions, let me know."* She wants to test the
grouping with a provider first: *"this is one of the things I'd like to test with a provider — how do
we find some identifier to group that within the diagnostic results."*

### "Plain-language label on clinical report names"

Kelly's example is the whole argument. The report is called *"breast diagnostic bilateral with
tomosynthesis"*, which she called *"kind of confusing"*, and then: *"maybe there's a way we can have
Orion attach a mammogram label, because that's what everybody will know it as. No user is gonna look
for the breast diagnostic bilateral with tomosynthesis. They're going to type in mammogram, then it
will specify the type. Maybe that's something else we can think about adding down the road."*

Two design surfaces, not one: the label on the report row, and what search accepts. Related existing
work: the user-friendly category naming in `Health Data Category_User Friendly Laungae.xlsx` and the
LOINC crosswalk on the 8/31 line.

### "Document titles are gobbledygook on both sides"

Raised against provider Orion source cards but Kelly confirmed it's the same on the patient side:
*"we get the same thing on the patient side, where it's this gobbledygook of characters."* Her ask to
Jayanth: *"are we gonna keep it as this long, like uninterpretable thing, or what are your thoughts
on that? Do we change the label, the title?"*

The constraint is real: there is no filename to use. Jayanth: *"We don't get the file name from
health data documents. So we kind of make it up using the practitioner name… I generate this file
name based on provider name, category of the document, which is HPI note and stuff like that. So I
don't know what 13849 is, but it concatenates a bunch of different categories."*

Kelly's proposed target, and her own deferral: *"nothing to do now, but we can say this is your — you
get the provider name, what it is, and the date, and maybe that's what the right label is."* She also
noted the redundancy costs space: *"it's basically repeated here, the same or similar portion of the
number… and just takes up extra space."* Refine it after Portu testing shows what notes actually
come through. Related: `sources-hybrid-row.html`, `sources-no-logos.html`,
`orion-source-chip-spec.html`.
### 9/8 addition — design review + team meeting **2026-09-08**

### "Reports tab grouping is due next Tuesday to Greg"

Kelly set the date on the sprint board: *"we'll make that due next Tuesday for your presentation to
Greg."* Yuehui folded it into one piece of work with the abnormal / normal grouping: *"this task I
will do with the abnormal and normal task together because it's the Health Hub upgrade. So I will
take it as one overall structure."*

Two people are blocked on it. Greg, on seeing the current state: *"I saw the basic list you did. I
thought you were doing something more, and we were also going to get the visual."* Jayanth: *"that's
what we're still working on, Greg. Yuehui will have a UI ready for it, and then I'll make the
updates. But right now, all we have is the basic list."* Greg's priority call: *"That needs to be
the first one you do because you're going to need that with the pilots."*

Kelly also caught that the out-of-range labs dev task was staged wrongly: *"out of range labs, which
should not be ready for dev actually, because you haven't completed the design."*


### 9/15 additions — design review with Kelly, Tue **2026-09-15** (47m, Jay's internet dropped)

#### "Rename needs focus to out of range across the whole Health Hub"

The 9/11 decision covered the reports tab. Kelly widened it while reviewing the handoff: *"I think we
were going to change that need focus section to out of range because we're not sure it needs focus."*
Two carve-outs she named explicitly. The **vitality score keeps its needs focus label** — *"you won't
change it on the vitality score, you're just changing it on the label for the reports stuff, right?
Because the vitality score says needs focus."* And anything **Orion specifically flags** keeps it:
*"everywhere else it would say out of range unless it's specifically linked to something where Orion
is saying needs focus. Because I can have an out of range lab, but I don't need to focus on it."*

#### "Jay reviews the Health Hub reports handoff before I show it to Greg"

Yuehui's own call, made when Jay dropped off the review: *"I have the finalized handoff version for
the health hub, like reports those screens. I think this part I need Jay's input a lot."* The plan is
to walk him through it offline before it goes in front of Greg.

#### "Reports tab and out-of-range labs UI go to dev"

From the team weekly the same morning. Jayanth's position was that out-of-range labs and the reports
tab already exist in both products and only the **UI updates** are outstanding: *"if you are talking
about the UI updates, then maybe we can push them down. But both out of range labs and report steps
are already there."* Kelly pinned the release: *"we had those prioritized as two for design, and now
you're saying UH is almost done with those, so those can move to dev now... within the let's go with
the October 9 release."* Jay confirmed.

Note the gap worth watching: Kelly told Greg *"these are done, which we'll get to you this week"* —
but at the design review an hour earlier the relabel was still to do and the handoff still wanted
Jay's review.

#### "Images inside an Orion question and file upload land in the 9/25 release"

Greg pushed on why Orion can't take a file or generate an image when the underlying models can.
Jayanth's answer is the one to design against: *"when we call their APIs, each one of the data, the
data pointer that we send to those APIs is a separate feature in its own. So sending a file is a
different feature versus sending a text message."* He agreed to include images-within-questions in
the **9/25** release. That gives the paused image work in this section something concrete underneath
it.



---

## Treatment Plan / Lifestyle Plan

Source: Greg's pricing / product meeting **2026-08-24** (where the feature was born, Greg in the
room), then the caregiver design review **2026-08-25** plus the team weekly the same day. Greg's term
is **lifestyle preventative plan**. This is the block Kelly wants a first pass on by Tuesday,
alongside caregiver.

Full extraction of both meetings, with quotes and the business rules that gate the design, lives in
`C4P_TreatmentPlan_Requirements-Brief_v1.md`. Read that before designing; the entries below are the
task-level version.

The patient-side proposal is `treatment-plan-patient-ia.html`, now at **v2** and matching the 8/31
Figma frames: placement decided (plans are a section inside Vitality, not a fifth chip, because a plan
does not feed the roll-up), the many-plans model and its tension with Greg's one-shared-plan ask, who
owes the patient a reconciled version, three frames for the states that do not exist yet, the four-state
mark, the dependency table and six agenda questions.
`treatment-plan-flow-board.html` is the same loop as a sticky-note swimlane board (provider / Orion /
patient, ten steps, four pink notes for the undecided parts), with
`treatment-plan-flow-stickies.md` holding the sticky text in FigJam paste-ready blocks — Figma's tools
in Cowork are read-only, so the board has to be rebuilt by hand there.

### What it is

A holistic plan across inside health, care and lifestyle, generated from Vitality data, reviewed and
adjusted by a provider, then tracked day to day. Jayanth: *"we keep saying that that's exactly what
vitality is, because vitality is a holistic overview of your inside health, care and lifestyle… at
the end of the day, we are using Vitality data."*

The loop: Orion generates → provider reviews and adjusts → patient sees it and can influence it →
provider tracks adherence.

### "Design the first-pass one-page plan view from Vitality data, and recommend where it lives"

Kelly's assignment, verbatim: *"why don't you mock something up of what the one pager would look like,
and then we'll go with where it goes… You suggest where the treatment plan button or view goes, and
then we go from there."*

- **Where it goes is genuinely open, and the two loudest voices disagree.** Greg does not want it
  replacing Vitality — Kelly: *"Greg was not on board with the treatment plan or lifestyle plan
  replacing the vitality page. He clearly wanted it to be a separate UI that is shown elsewhere,
  linked from the homepage."* Jayanth wants exactly that replacement: *"I still think we should
  replace the vitality tab to treatment plan… we still show the needs focus. We just change the name."*
  Yuehui's proposal on the table is a **fifth tab** — treatment plan / verified by provider — keeping
  Vitality first as the overall evaluation. Your recommendation settles it.
- **Both halves.** Yuehui asked whether it's tracked goals or a static text plan. Jayanth: *"Both.
  Greg wants to see a snapshot of the overall summary for the patient, like what they need to focus
  on — that would be in text. But they'll also see all the goals and how they are tracking."*
- **Keep the prose short.** Kelly: *"it may be more convenient visually, so it's clear what the actions
  are versus the long paragraph to read. Because I wouldn't get that."* Yuehui's answer, which Kelly
  called a good example: *"you have your provider's treatment plan goal of your daily steps. We can
  just directly show it in the steps and the data tracking. We can set a goal for them so they don't
  need to read any text."*

Greg's own requirement is one page: *"I need one page that shows me everything that I need to focus
on. Right now, I have to click on two, three different things."*

### "'Verified by your provider' tag on individual goals + a filter for the verified ones"

Yuehui's counter-proposal, and the strongest idea in the meeting. Her argument: *"the treatment plan
is more like a backbone behind our vitality system. It's not another single redundant duplicate of our
vitality system… meds, diet, your daily activity is already across our vitality system… the valuable
stuff for the user is 'this goal is verified by your provider.'"*

Mechanic: tag individual goals as verified by provider, plus a filter for all provider-verified goals.
Kelly agreed and merged it with the one-plan model: *"typically the user can add their own independent
goals that would then be part of your visit summary that you talk to your provider about. So it still
should be an all-one plan, but I like your idea, just an indicator of which ones you've already
discussed or been approved by or set/ordered by your provider."*

- **Conflict case.** Hers: *"my weight management probably conflicts with my original last year's
  treatment plan from my provider."* Detect and surface it.

Related naming distinction Jayanth wants preserved: a **physician-reviewed** plan (Dr. Portu actually
reviewed this patient's plan) versus a **physician-backed** plan (the generator was shaped by provider
input across all patients). *"Two different product landscapes."*

### "Prevention elements -> trending the wrong way, not only out of range"

See the Health Bio & Stats block — same mechanism, different surface. Kelly: prevention lives in the
plan as *"actions or monitoring or to-dos"*, and eventually as standing orders (*"I need these four
labs done. So it's in the plan already. Just clicks the button."*).

### "Provider adjusts Orion's plan"

The two canonical cases, keep them in the spec: *"I see why you suggested the patient should walk
10,000 steps, but maybe they should just walk 5,000"*, and *"I see why you suggested 200 grams of
protein, but they don't have proper kidney function, so they have to do only 50 grams per day."*
The patient can push back too — *"they have a nutrition plan, and they want to say that I don't like
broccoli."* Provider then tracks adherence day to day.

Today only the meds goal is implemented; sleep, activity and diet / nutrition goals are coming, and
the plan assumes them.

### "Revise the Vitality landing page -> needs-focus goes nowhere right now"

Jayanth's framing of the whole effort: *"this is essentially vitality landing page, but better vitality
landing page."* The concrete defect: *"if we click on that needs focus, there is nothing there. It's
just explaining vitality… it's an empty screen almost right now."*

Kelly's sketch of the fix, which doubles as the argument to bring Greg: *"these could say in the top,
inside health needs your attention for these three items, and then these two are fine, and then this
is the detail for your treatment plan."* Her read on Greg: *"maybe he's not clear that there's really
nothing behind this, and then this brings it all together."*

Four tabs today: Vitality, Inside Health, Care, Lifestyle.

### "Name it"

Unsettled. In play: lifestyle plan (Greg's preference), treatment plan, preventative plan, lifestyle
treatment plan, verified by provider. Jayanth's objection to Greg's: *"I'm confused when we say
lifestyle because we already have a lifestyle thing."* And on the current name: *"maybe we shouldn't
call it vitality because nobody understands vitality."*

### "Premium vs. base for the plan is still open"

Blocked on a business decision, not a design one — but it changes what the caregiver view can show.
Jayanth in one breath said base sees no treatment plan, and in another that *"patient base mode should
have access to that treatment plan"* under the provider-pays model (~$5.99/month per generated plan,
provider bills the payer). Kelly: *"I think base treatment plan hopefully will be included because
otherwise view won't be as useful."* She's writing the model up. Design both states until it lands.

Ethics constraint both agreed on and worth designing around: the provider must never be the one
pushing the patient to upgrade. Jayanth — *"Anything that puts the provider on hook for patient
signing up is a kickback."* Kelly is separately working out compliant billing and treatment-plan
language.
### 9/8 block — design review (Kelly, Jay) then team meeting (Greg)

**Where this landed: Greg did not sign off.** Kelly asked directly — *"Do you want to sign off on
this direction? Do you want to see it again?"* — and he answered *"Well, the only thing I'm still
missing is that single snapshot. This is just a lot of setup stuff, right?"* A second review was
agreed (*"bring it back to Greg for sign off"*) and never dated; Kelly owns scheduling it. Jay's
two-week build starts at sign-off — *"once we sign off on the draft visual, you think it'll take you
about two weeks"* — so the revision is the critical path to the pilot.

**What survived intact:** the six categories. Jay's own build list is *"workout, sleep, medication
adherence… screenings and vaccine recommendations"* plus *"dietary recommendations. Yes."* — the
same six. Kelly on the whole draft: *"this is on track from a high level."* The open questions are
written up in `Design-Questions-2026-09-08.md`.

### "Call it the preventative treatment plan"

Greg, first words on the design: *"I don't want to call it a treatment plan. Let's call it
preventative treatment plan… We need word preventative in here, right?"* Settles the naming line
from 8/25 and the billing requirement behind it.

### "Conditions and immediate treatment requirements go on top, above the goals"

The change Greg pushed hardest, and he had to say it three times before it landed. *"it would seem
to me you'd want to generate first the medical issues that they got to worry about that are
treatments… the known treatment requirements… This is a necessity, and then goals are over and above
that."* Then: *"you miss my question. It needs to start with what's the thing. What's the problem.
So the problem is I've got four alerts: calcium, red blood count, platelets, and glucose levels, and
it should then say, and I also have additional goals other than that."*

His definition of why the page is called preventative: *"there should be a summary real quick of what
are the immediate treatment requirements that you have that you can't ignore. That's why it's a
preventative treatment plan — because you have preventative steps to make sure you don't have a
problem, and then you have problems you also have to take care of."*

Confirmed as the opening block: Yuehui *"It will be on the top. The condition."* Greg *"Perfect."*

- **Known vs projected is part of it.** *"the dashboard would say, what are all my medical
  requirements to be met, both known and projected? So projected is one more lab, and I'll be
  pre-diabetic at the rate I'm going."* A projection is a requirement, not a goal.

### "Provider sets the high-level goals, patient builds the detail with Orion"

Decided. Greg: *"He should be able to say, here's your high-level plan. Create the detailed plan that
we can monitor."* And: *"the doctor set that as a goal, and a goal is to lose how many pounds. And
then on the patient side, it gives different options for diet programs to lose that weight."*

Kelly's restatement, which Greg confirmed with *"right"*: *"the doctor initiates the goals and signs
off on them. The details of how the patient achieves those goals is curated by the patient."* Her
three-legged summary: *"provider initiated and Orion curated with patient input."*

- **The diet example is the model for the whole tier split.** *"the doctor goes through and says you
  need to lose 10 pounds. You can do that through a balanced diet… or you can do with a low carb
  diet, and the patient should be saying which one I want to go on, but it should also say you
  cannot do the caveman diet… All three are weight loss programs, but one of them creates huge
  problems based on his medical record."* So a row carries a provider-set target, a set of allowed
  methods, and a forbidden one.
- **Preferences reach the provider at creation, not after.** Kelly: *"If the provider is
  recommending a low carb diet or a high protein diet, but the patient is plant based and may
  struggle to maintain that, we need to make sure the provider knows… as long as the information's
  there when the provider creates it, that may impact the goal the provider is creating."*
- **Unreconciled with the paywall answer** — see the base / premium line below.

### "Provider snapshot on desktop is the sign-off gate"

The single most important thing to come out of 9/8. Greg's ask, in full: *"Is there a single
dashboard for the next meeting with the doctor that shows the goals, the plan objectives that he set,
and then the measurements that the user set up compared to the planned outcomes. One single dashboard
to just quick snapshot of — I give you a plan, you fulfilled the details of the plan, you've been
working actively towards the plan, and here's where you're at right now."* And: *"One single view.
So here you got all the details that the patient needs to work through to get his plan. The doctor's
just going to see a quick snapshot."*

Kelly pointed at the existing home-page card as the answer and he rejected it: *"The snapshot is on
the left on the home page. Your treatment plan with Dr. Irene Medina — that's the single snapshot"*
→ *"Well, it still doesn't appear to me that you really have set…"*

**What has to be on it**, from his own list: known and projected medical requirements; personal goals
(*"better sleep, workout, diet, blah blah"*); labs, only the ones out of line, compared then versus
now, with the projection off that; symptom resolution (*"it should also include the symptoms to see
whether the symptoms have gone away"*); and outcomes against both the plan and the insight (*"if
you're going this way on glucose, when he comes back in, it better have gone down"*). His bar for
the copy: *"This is what I told you to do. Here's how well you're doing it. And just saying 'stable'
isn't going to cut it."* His critique of the current metrics row: *"I don't really know, other than I
have X number of steps and I eat X number of carbs… if you're on a no carb diet, better not be
eating 72 grams of carbs. No carb diets are less than 20 carbs a day."*

**It is a desktop provider surface.** *"you're limiting yourself to the phone here. The real
dashboard that I'm talking about is for the provider to review how the patient is done with all this
data already being in his snapshot that's going to run on the computer. May have a smaller version
for the patient… the doctor wants to see it in clinical speak anyway."* That makes it a different
build from Jay's two weeks, which is why Q2 in the questions file asks for the release split.

### "Restructure the top level to progress-to-goal"

Kelly's reframe, and it is the one that makes Greg's ask affordable: *"maybe we can rethink those
categories we talked about last time and do it from a progress to goal perspective. So if my goals
are to lose weight, I don't really need to know how many steps I took. Am I following my diet and
exercise programs? Meaning, I'm eating healthy and exercising X days a week, and I've lost Y pounds.
Maybe that's all the doctor needs to know… that's the high-level monitoring progress to goal. But all
the stuff you have in there is great because that's the click-through detail."*

So the six category cards do not get thrown away — they move down a level. What goes on top is
goal → adherence → outcome, plus the symptom line: *"at the top, it might be a symptom like, has my
hip pain resolved? And that might come back to the screenshots I sent you on how am I feeling
today… then we're just tracking to that — symptoms resolved or lessening would be the monitoring
piece that the patient and provider would see on the one pager summary."*

### "v1 evaluation is pass-through, not a C4P scoring engine"

Yuehui raised the cost twice. First: *"I want to confirm what I'm understanding from Greg's
perspective. So that means we need to move further, like have a tracking or even evaluation system…
because I just intentionally removed the specific tracking system for each category, because I assume
it needs a lot of time to build underneath."* Greg cut in with *"all of the detail is necessary"* and
a monologue, which is a scope expansion, not an answer. Second: *"how can we evaluate your overall
sleep, and beyond that we need to evaluate how did you do to target your treatment plan goal… we need
to map on the different evaluation."*

The two things he actually said, both of which read as permission: *"I think you just steal Apple. So
Apple gives you average sleep over seven days. Apple gives you average workout attainment over seven
days… I would just grab that same information and convey it."* And: *"I don't care whether you
calculate in our system. I'm just suggesting that they average everything for you."*

Kelly, whom Yuehui asked directly (*"I don't know, Kelly, if you have any thoughts on that. Like, how
can we start?"*), did not answer — she redirected to Jay and Portu. So this is Q3 in the questions
file, with a written default: seven-day averages for activity and sleep, adherence percentage for
meds, then-vs-now for labs, patient-reported for symptoms. Nothing else.

- **Start from meds** — Yuehui's own proposed starting point, unanswered: *"probably start with the
  meds, because meds we have the goal and we prepare for the daily log, so we have the data to
  contribute to the tracking and evaluation system."*

### "Fix the adherence numbers"

Kelly, in the design review: *"the med overall number of 80% should match the everyday, every dose
number of 95% adherence. So those should be the same, right?"* and why it matters: *"if it doesn't
match in the demo, that could be confusing."* Either reconcile them or label both explicitly.

### "'Recommend' becomes 'consider'"

Kelly: *"instead of recommend, can you say consider? … we're getting away from Orion is the doctor…
talk to your doctor about versus would you consider."* Applies across the plan copy, both sides.

### "Preference tag, not a preference editor"

Jay opened with preferences as a gap — *"if I wanted to say that I don't do strength training, I only
do cardio, then the strength goal should be adapted"*, and *"Greg keeps saying the preference in
terms of diet — that he hates cauliflower, and if Orion says eat cauliflower, then he wouldn't like
it"* — then reversed himself and landed somewhere better: *"all the preferences are not associated to
the treatment plan. The preferences are associated to Orion and users, Orion chat history. So
whenever Orion generates this draft plan, it should have already considered the preference… and we
don't have to change anything here."*

His residual idea, which does imply UI: *"maybe it's a user preference tag that we use across the
board, and therefore Orion makes the decision based on that user preference."* That tag, on the
affected row, is the minimum design and it is the default written into Q4.

Greg's version of the same requirement, for the record: *"You can tell me asparagus is all low carb
and it's good for you, and I'll tell you to go screw yourself… You want me to get out of the program
altogether? Tell me I have to eat Brussels sprouts."*

### "Catch-all provider field for what the six categories miss"

Greg's pain-management case: *"entire practices that are nothing but pain management that do different
types of cortisone shots… you go into an appointment at a doctor's office for a shot. They put you
under for these shots. These are not medications you take at home."* Jay wanted it under medications;
Greg refused. His scope warning: *"you're basically taking orthopedic off the table if you don't add
in pain management and physical therapy."*

Closed in favour of a custom field. Jay: *"the simplest thing I can think of is adding a custom field
for the provider, a custom category that the patient can track on their own, and they can say whether
they are aligned to it or not aligned to it."* Greg: *"something you use for catch-all other things we
didn't think about"* and *"I think custom one's no brainer."*

Kelly dissented and still intends to test the alternative — using the EMR's existing treatment-plan
field — because *"for any office that's already using that field, they'd want us to take it from
there… You don't want to change their workflow unnecessarily."* Jay's counter: *"We don't even get
that data clearly, so I don't want to depend on that… I wouldn't even trust that."*

- **PT combines with workout later.** Greg: *"We can just combine workout and physical therapy."*
  Jay: *"we can definitely combine physical therapy with workout at some point, but we have to start
  with workout first."*

### "Labs and check-in cadence belong in the plan"

Greg wants the plan to issue the next lab order: *"maybe put in the preventative plan — prior to
every next meeting you rerun your labs so that you get a fresh, updated picture of those outcomes."*
And: *"the monitoring can't just be what we get off the watch. It really needs to be also against lab
results. So part of the doctor's requirements are: what are the labs, and what is the time frame that
you're going to run that test prior to my next appointment."* Why he cares: *"that flips the entire
doctor's process on its ear in a very positive way. Instead of talking to me about the next symptoms
and determining whether I should go run some labs — it's already got all the goals, already knew what
it was trying to accomplish, and already ran the labs. And now I'm spending all my time reviewing
outcomes and tweaking the requirements."*

Plus meeting cadence: *"maybe part of the plan should also have a level of frequency to meet with the
doctor"* → Kelly: *"Check-ins, and they can be virtual or in person."* This is the same shape as the
8/31 line about labs as a goal with a cadence.

Also raised and parked: significant alerts to the provider (*"your watch catches your AFib would be
something the doctor wants to know about"*), which Kelly put on the messaging roadmap while asking for
design thoughts.

### "Base can't see the plan, premium can see an Orion-generated one without a provider"

The contradiction, in two quotes forty minutes apart. Greg on the paywall: *"in order for us to
guarantee these premium upgrades, they don't get to see the prevention plan on their side if they
don't have the premium"*, then *"if they don't sign up to the service, they won't be able to see the
plan on their side. They'll only be able to review it with you next time they come to the office."*
Jay: *"If they have the premium, can they see it even if they didn't get it from a provider?"* → Greg:
*"Yeah."* → Jay: *"Okay, so it will be flagged as generated by Orion."*

Then at 1:03 the agreed flow was *"start point is still from provider."* Both cannot be v1's entry
point. This is Q1 in the questions file. Note Jay relayed it as Yuehui's question at the top of the
meeting — *"the one question that Yuehui brought up today was: do we show the treatment plan even if a
provider doesn't actually prescribe it, as a draft treatment plan from Orion, or do we only show it to
the patient if it comes from a provider? That's a question I guess we need to answer first, Greg"* —
and the answer that came back was about money, not about verification.

### "Workout and recipe programs pulled in and customised to the record"

Greg, expanding scope well past v1: *"we can also call in a customized workout program. Be great if
they sign into our app every morning and use it to do the workout program with it."* And: *"I really
want a link that allows us to pull in diet books, recipes by day, workout programs, both of which has
some logic to customize it based on the medical record of that patient."* His competitive claim: *"with
Connect for Patients and V Shred, you have the only customized workout program on the market.
Customized directly to your medical conditions."* Kelly's cheaper interim: *"they just link to their
Peloton and that updates their goals for now because we have basic goals."* Stays paused — same as the
8/24 third-party content line.


---

The lines below come from the **8/24** meeting with Greg. Everything above is the 8/25 reinterpretation
of them by Kelly, Jay and you.

### "Greg's page content, top to bottom"

His own stack, in his own order: *"goals: lose weight, eat better, fix glucose, blood pressure, heart
disease, whatever the medical plan is. Underneath that, it says, okay, here's the treatment for these
medical issues. Here are the diet and workout programs and medications you need to take to address
this, and here's the trending of the current and past labs, and then here are goals that are in
addition to that that I might have."*

Also on the page: *"here are the key problems in the lab results, in your radiology reports"*, plus
dietary and workout monitoring.

- **Every goal needs a target, a timeline and a baseline.** *"It's got all the trending. So it's got
  this starting point, and then it keeps trending until you've exceeded or not on your goal plan."*
  And: *"the goal needs to have a timeline you're trying to do it within."*
- **Before / after framing.** Lifted from how diet and workout programs are actually sold: *"they show
  you before and after pictures of everybody… so you're trying to create that. What's your current
  before, and what do you want your after to be?"* The same shape becomes marketing later —
  de-identified before / after labs from a finished plan.
- **Drill-down, not duplication.** *"Every one of those click downs, you already have. How am I doing
  against the plan?"* And the division of labour he insists on: Vitality keeps scanning the whole
  record for new problems (*"we don't want to get away from the thing that's looking at everything"*),
  the plan measures only what the doctor and patient agreed to.

His summary of the whole ask: *"I just want one more UI that's generated on the goals that are set both
by the doctor and the patient."*

### "Provider builds the plan on desktop with the dashboard's drag-and-drop framework"

Greg asked directly: *"I'm hoping that we built that drag and drop user defined framework. Is there any
reason that same framework can't be viewed on the patient side, Jay?"* The plan is assembled per
patient — *"it literally needs to be created on the fly for each patient"* — by dragging in the goals
and elements that apply.

- **This is the provider side.** The builder lives in the provider dashboard, on desktop, during the
  visit. Jay flagged that drag and drop is hard on phones. Greg: *"you can only build it on the
  computer, but you can display it on the phone. You can't even build a new plan on the phone."* And:
  *"at least in the first release, do we need the phone to have the ability to configure a dashboard?"*
  Kelly's answer: *"start with the treatment plan. Do it."*
- **Note what Greg actually asked**, because it is narrower than it sounds: *"is there any reason that
  same framework can't be **viewed** on the patient side, Jay?"* He was asking about rendering the same
  widget structure on mobile, which is why Jay answered *"showing the view is not a problem."* Framework
  reuse on the patient side is a rendering question, not an editing one.
- **Whether the patient ever rearranges their own plan is Jay's open item**, not settled here: *"we can
  let you know when she builds the treatment plan landing page, the ability to see if we can leverage
  the same drag and drop functionality to allow users to edit stuff."* It sits behind your first pass.
  Separate question from where the plan view lives, which is yours to recommend.
- **Why creation is desktop and in-visit:** *"it's something you do with the doctor because the doctor
  needs to be able to bill for this."*
- **Kelly's mobile alternative**, still open: *"maybe we have a select option to pin things versus drag
  and drop."* She thinks it fits patient functionality better than drag and drop. Cross-ref the select
  / pin pattern already used elsewhere.
- **Patient edits inputs, not layout.** Greg: *"they're more input on what they've done."* His examples:
  correcting his own weight, and picking which of two conflicting prescriptions he actually takes
  (Lipitor 80 from one doctor, 20 from another). From 8/25: *"I don't like broccoli"* in a nutrition
  plan.
- **Resolved symptoms drop off on their own.** *"If I've got symptoms that go away… an easy way to get
  to the things that are changing, and it immediately changes the dashboard."*

### "Plan gets amended at every visit"

*"You're adding and subtracting things against that formalized plan every time you meet with a
doctor."* The plan is the patient's lifecycle record, not a snapshot: *"here's everything that's been
wrong with you that's still there. Here's what you've been doing. This is the success or failure for
each one of them."*

At the visit it becomes the agenda: *"what did we agree to, you and I, Mr. Patient, and let's see how
well you've done."* Greg wants the accountability conversation on purpose: *"gonna be interesting when
it says quit smoking and the guy didn't, and eat this diet and the guy didn't, but it's the kind of
discussion you want to have."* And the doctor's new question: *"why does that new symptom exist if I
did this plan and adhered to it, or is this something new that I need to add into the plan?"*

- **Provider surfaces named.** A summarized plan view the doctor reads right before the visit
  (*"doctor can see it right before the meeting in a summarized form"*), and Kelly's treatment plan
  link in **visit essentials**. She extended it on 8/25: the provider snapshot should be current
  conditions, care needs, lifestyle elements, then alignment to the treatment plan.
- **Audit trail as a control feature.** *"If you want, we can put in there the ability for the doctor
  to say, I want to see where else this guy went drifting off with the AI, so it addresses the control
  concern."* Design question that follows: does the patient know the doctor can see that?

### "Share the plan across doctors and specialists"

*"I don't want this plan to be just between the primary and the patient. I want to have the ability for
other doctors and specialists to be able to share that plan with each other."* His reference case is
Roque at Southwest Medical Research: eight doctors adding real-time information with no way to
collaborate — *"everybody's just adding different information, and we have no way of collaborating on
how all this relates to each other."* Overlaps the sharing and care-team work.

### "Known useful supplements section off the labs"

Raised as his *"last thing"* on 8/24. *"If you look at the labs, I bet you we could have a section that
says known useful supplements."* The frustration behind it: *"the doctor is measuring my inflammation
but he's prescribed me zero to do about it."*

His examples, worth keeping as the spec's test cases: turmeric for inflammation, glucosamine for joint
pain, and L-arginine, which he researched himself rather than accept a CPAP mask after a sleep study.

- **Show the backing research.** *"The doctor would have to believe these are good supplements, so we
  should have the backup research for them."* So each recommendation needs a source, not just a name.
- **Two ways in**, Kelly's framing which Greg took: *"here's some things that you might want to suggest
  for your patient, doc, and put in their plan"* — Orion to provider — *"or things the provider
  recommends directly."*
- Kelly also wants supplements in **suggested questions**, and flagged a billing angle.
- Payer argument Greg likes: *"instead of prescribing expensive drugs, you're buying supplements that
  they don't have to pay for."*

### "Diet and workout need real content"

Greg's test: he asked Kelly how you reduce glucose, she said eat less sugar, he wanted the other half —
*"your glucose goes down a lot faster if you get on a good workout program."* Conclusion: *"we need to
get a little clearer on the diet and workout piece by actually telling them recipes and potential
workout programs they could consider."* At plan creation Orion has to be able to say *"you want to
follow these kind of guidelines on your diets and this kind of workout programs."*

- **Third-party programs — Pause, his own call.** *"I want to start calling on social media people that
  are big in workout programs, dietary programs, so that we can use their programs but adapt them based
  on our medical information. That we don't have to do right away. I want to get the plan in place
  first."*
- **Food photo — Pause.** *"Eventually you're going to be showing proof of how many calories and how
  much fat you ate, based on the technology where you can take a picture."* Which turns into
  monitoring: *"did he stay off the sugar? Did he eat enough protein?"*

### "What I can and cannot do with my condition"

From his own injury, and he's angry about it: *"if it's got a radiology problem like mine, it would also
show me all the what I can and cannot do based on my condition. Which, by the way, I have had zero
support from doctors on this."* Hospital gave the wrong answer, primary sent him for new tests, two
weeks before anyone could tell him what to do *"other than don't walk around."*

Hangs off the anatomy-visual item in the Reports block: Orion generates a picture from the radiology
report, and the do / don't guidance sits with it, inside the plan.

### "The plan demo in the auto-onboarding flow"

Greg's distribution path, and Jay's action item pairs it with the plan landing page. Bulk-load a
practice's records, generate an account per patient, email an invite with a temp password, they
download the app and land in a populated app. Then: *"we give them an immediate demo of the services
that are available. One of which is this new plan concept that you will talk to your doctor about the
next time you see them."* Also promoted in that flow: caregiver services, family history, Orion for
research.

Two design constraints on it. It repeats — *"we don't do it once, we continually refer to them"* — so
it needs a non-annoying pattern. And the kickback rule means the upgrade prompt can't be framed as the
doctor asking for money: *"this is a service that your provider is offering for you, and mention
nothing about price."*

### Added from the design review Mon 2026-08-31 + the Greg meetings Tue 2026-09-01

Three calls: the 8/31 design review with Kelly and Jay (treatment plan runs 0:54:47 to 1:39:56, and the
real argument is in there), the 9/1 team weekly where Greg added to the scope, and the 9/1 caregiver
walkthrough where he approved the caregiver work and told you to move on. Full extraction with quotes
and timestamps: `C4P_TreatmentPlan_Feedback-Extract_2026-09-03.md`.

The headline: **the replace-vs-backbone question you asked twice did get answered**, by Jay, without
anyone labelling it as an answer. He rejected two parallel systems outright, then argued Vitality
already produces plan content and lacks only three things: *"It just doesn't display it as goals or
goals that can be tracked and goals that can be reviewed by your provider."* You restated it back to
him and he said *"Exactly."* Note this is the same position you took yourself on 8/25 ("more like a
backbone behind our vitality system"), so it has been your read from the start.

#### "Decided in substance, never ratified -> Jay doesn't care about the label"

Jay, 1:20:51: *"we just either we change the vitality tab or we change the vitality landing page to
call it treatment plan, or we add another thing called treatment plan. I don't care, but at the end of
the day, it's the data coming from Vitality."* Your 8/31 decision (a section inside Vitality, not a
fifth chip) is compatible with all three of his options and is the least disruptive of them. Nobody
said yes to it out loud, so it is worth stating as a decision at the Greg review rather than leaving
it to be discovered.

Kelly deferred when you asked directly at 1:30:27: *"I think you're right to question that. I would say
for now, let's create a one-page treatment plan. It should be aligned to the vitality goals, but maybe
we have to go back and rethink that down."* Read that as deferring the label, not the model.

Greg gave a third quiet vote on 9/1 without being asked. On caregiver alerts: *"the alerts that I'd
want to look at as a daughter taking care of dad is just the vitality section, right?"*

#### "Scope the first draft to four buckets"

Jay's list, 1:25:21 and again at 1:28:14, chosen on one criterion: what a patient can use today with no
provider involved. *"I can use medication adherence as a user or a patient. I can use diet or nutrition
recommendations. I can use workout recommendations. I can use vaccine recommendations. That's it. Like,
let's go with those top four."*

His gate on everything beyond that, same passage: *"if we are building this because we know that we can
pay for it, or we think that we can ask the providers to pay for it, then let's confirm that. While we
are waiting on confirming that, let's not over build this."*

Kelly's boundary, 1:31:19: *"just do these categories, add the clarity for how we either separate"*
prevention from vaccines.

Per bucket, from Kelly at 1:22:56 and 1:32:18:

- **Prevention / screening** — "You're up to date. You're due for X", linking to the vaccine or
  prevention page. Jay confirmed the engine exists: *"caretab tells me I have to take a vaccine, flu
  vaccine this year."* It is age / gender / condition driven and de-duplicates against procedures
  already recorded, so it will not tell you to get a mammogram you already had. **Your open call: one
  bucket or two.** Kelly's worry is that prevention-and-screening as a single category has never been
  built, while vaccines has.
- **Medication compliance** — "yes, you're taking all your meds on time." The design exists and is
  approved; Jay is building it now. Do not redraw it.
- **Diet** — the doctor's order at the top (*"eat a low-carb diet, aim for under 65 grams of
  carbohydrate a day"*), Orion's curation underneath (vegan, allergic to eggs, gluten free). Recipes and
  weekly plans are a second click. Kelly's open question: *"does the person really want recipes and a
  daily plan, or do they just want a list of foods that are part of their diet?"*
- **Exercise** — basics only, linking to PT orders where they exist. *"we're not going to show the
  exercises on the treatment plan."*

#### "Add sleep as a bucket"

Greg, 9/1 at 0:36:57 and 0:37:33: *"that sleep is part of the base plan"* ... *"definitely need sleep.
Sleep is one of the most important things, right?"*

Worth knowing how this went, because it changes what "we don't have the data" means: Kelly pushed back
thinking sleep was unavailable, and Jay corrected her — sleep **is** monitored. The bucket that has no
data source is **stress**. So sleep is in and stress is out, which is the opposite of where that
exchange started.

#### "Buckets have to be configurable"

Greg, 0:37:54: *"let's build that goal orientation, and then monitoring buckets configurable, where we
can add new categories or buckets based on what we come up with in future."*

Design consequence: the categories are not a fixed five-row layout. Whatever container you pick has to
absorb a sixth and seventh bucket without a redesign. Showing a 4-bucket and a 7-bucket state in the
same frame set is the cheapest way to prove that at the review, and it pre-empts the question.

#### "Labs as a goal with a cadence"

Kelly, 1:27:21: *"make sure you get your A1C every three months. That's the goal that a doctor put in
for diabetes. They write a specific goal. You could start with something simple like that."*

This is a different shape from the four lifestyle buckets: doctor-authored, a recurrence rather than a
daily target, and no device data behind it. It may be the cheapest version of condition-specific goals,
which is otherwise deferred.

#### "Design the three plan states"

The most consequential thing to come out of 8/31 and it was not in the v1 brief.

Jay's problem: if a plan only exists when a provider makes one, almost nobody has a plan and nothing
ships until billing is confirmed. His fix, 1:17:03: *"did we say that treatment plans will be something
like needs to be reviewed by your provider? They would have a status... So if we do that, then a
treatment plan can be generated by Orion for everybody using vitality information."*

And 1:20:21: *"it's one thing to say Orion generated this. This may or may not be true. We'll add a
disclaimer saying that consult with your provider before approaching these. And if the provider reviews
it, we make it bright green and say, hey, this plan has been reviewed by your care provider."*

So three states, and the unreviewed one is the **default**:

1. **Orion-generated, not reviewed** — disclaimer on by default. Every patient with connected data.
2. **Reviewed by your provider** — Jay said bright green. Check that against the status tokens:
   `--color-status-success` at `#10b981` may be quieter than what he is picturing, and green already
   means "in range" elsewhere in the app, so review and in-range would collide on the same screen.
3. **Provider-authored / adjusted** — the billed version, where a target was changed.

Jay also floated a route to state 2 that needs no provider builder, 1:28:14: *"maybe the patient goes to
the provider, shows the C4P plan and asks him to review it. That's also a way, and he can manually
update it."* That is the only reviewed-state path that works before the provider dashboard ships, and
it has no design yet.

#### "Draw both frames for Greg"

This state model quietly changes who the feature is for. The 8/24 brief has the doctor authoring the
plan in the visit and billing for it. The 8/31 model has Orion drafting it for everyone and provider
review as an upgrade. Both can be true eventually, but the mockup has to open with one of them.

If the default frame on screen is "your provider built this", it will not match what ships first. If it
is "Orion drafted this, unreviewed", Greg may hear it as giving away the thing he wants to charge for.
Put it to him as a question with both drawn rather than choosing quietly.

#### "Single plan with the conflict raised inside it"

**This reverses your 8/31 mockups.** Both Kelly and Jay argued against multiple concurrent plans, in
the same meeting, independently, and neither had seen the other's reasoning.

Jay, 1:11:40, the concrete failure: *"what if my cardiology treatment plan says step count 5000, and
what if my weight management plan says step count is 10,000? So it gets messier when you're thinking
about it from multiple plans perspective."* Plus his read of Greg: *"Greg kept saying one snapshot of
everything that they need to do."*

Kelly, 1:05:18: *"we don't want a primary care plan and a specialist plan. We want, I'm one person, I
need one plan. And when there's discrepancies, those would be raised within the plan. Like, hey, you
need to talk to Doctor So and So, or these doctors need to talk."*

Read Kelly carefully: she did not reject the reality your mockups were modelling, which is several
providers with several agendas. She **relocated** it. The conflict becomes an item inside the single
plan, not a second plan. That is a smaller design than a plans list plus reconciliation, and it lands on
the page Greg asked for.

What survives from your version: the per-item provenance mark ("verified by your cardiology plan" on a
nutrient row, "associated with your weight management plan" on a meds row) — Jay's model needs it more
than yours did, because a single plan sourced from several providers still has to say who set each
target. And history, because amended-at-every-visit is a Greg non-negotiable.

What loses its reason to exist: the plans-list screen, and the cross-plan focus summary as a separate
thing. Both are re-tagged Blocked rather than dropped, because Greg asked for one plan in the first
place and has not seen either version.

#### "No plan number Vitality doesn't also show"

Jay's own test, 1:11:40: *"in your treatment plan, if I say your steps are you need to do 9000 steps a
day, that's because in your lifestyle summary it also shows that 9000 steps a day for a specific
reason."*

Useful as a design rule, not just a data rule: a plan goal is a **promoted** Vitality recommendation,
never a parallel entry. If a goal appears on the plan that has no home in Vitality, either Vitality is
missing a category or the goal does not belong in v1. Vitality keeps its own job, general "are you
healthy" evaluation against population norms, which was your distinction at 1:15:37.

#### "Entry surface answers 'am I on track today' without opening a category"

Your instinct that "one pager" should not translate literally to the screen is right, and you can
defend it with their words rather than yours.

- Kelly, 1:07:14: *"a visual, cool guide that when you drill into it, it takes you to one of the other
  screens we already have, like a vitality or a lifestyle or a stats or a med adherence."*
- Kelly, 1:32:18: *"maybe we have a secondary click that says create a weekly or monthly plan... That's
  not going to be on your treatment plan. That's a second click."*
- Greg himself, 9/1 at 0:35:12, on ingested recipe content: *"make it available in that one pager, **or
  click off that one pager**."*

So the promise is about hunting, not scroll length. Jay's restatement of the complaint, 1:20:51: *"right
now, I have to go into Inside Health, Care and Lifestyle and read through the summary to tell you what
my goals are."* Three places to look is the problem being solved.

The one thing it does constrain: if a patient has to open a category to find out whether they are on
track today, the one-pager promise is broken however few screens there are.

#### "Make it visual and fun"

Kelly said it three times, so treat it as a requirement rather than encouragement.

1:05:18: *"something a bit more visual with high-level kind of goals for diet, exercise, condition
summaries... It would say your treatment plan is to comply with your medication, get optimal sleep,
follow this diet, and follow this exercise regime."*

1:27:45: *"I think less is more in this case. Yuehui, like thinking about how Greg's always kind of
poking at me, of or yelling, too much, take that out. This one is really how do we make it look good,
fun to interact, want people to get their dopamine hits from following their treatment plan."*

1:30:19: *"make this as flashy and as fun as possible."*

#### "Widget-style composition for the patient plan"

Inside the 1:05:18 quote: *"kind of like the provider screen where you have this dashboard, and it's
everything about the patient that the provider needs to know and can customize it per the widgets. Same
thing for a treatment plan for a patient."*

Second time someone has suggested the patient plan borrow the provider dashboard's composition model —
Greg's drag-and-drop builder from 8/24 was the first. Still parked behind the release-1 rule (patient
side displays, does not configure), but it is now on record from two directions, which makes it likelier
to come back.

#### "Configurable med alert with a user-defined tolerance"

From the 9/1 caregiver walkthrough, 0:15:24 onward, and it belongs to med adherence so it lands in the
plan too. Greg: *"you don't want to find out tomorrow they didn't take it today. You want to find out
they're supposed to take it at noon, at two it's saying they have not taken their medications."* Then:
*"just an alert that comes within a user-defined tolerance level to make sure they take it today, not
find out tomorrow, and they skipped it."*

Your answer in the room was an evening backend sweep, which is exactly the next-day pattern he was
rejecting. The tolerance is per-schedule and set by the user, not a global cron.

Kelly closed the loop on routing: *"we did talk about that for the user, but it of course makes sense
that it goes to the user and the caregiver. Any alert notification."* Greg: *"it's bigger benefit to the
caregiver."*

#### "Image generation needs a job before it needs a design"

Kelly parked it, 1:38:16: *"Let's start with the first four, and then come back to the condition and
image thing... We need to brainstorm a bit more on what does this do? What's the purpose? How does it
get displayed? Why are we generating it? So let's not make that a barrier today."*

Jay's account of what Greg actually wants, 1:35:55: *"he almost wanted to replace the body... in his
mind, the 3D body map is not working for the conditions and procedure view, and he wants to replace that
with ChatGPT image generation... He said it should be associated to treatment plan, but the first version
of image generation, maybe we just show it in conditions and procedures instead of the body map."*

So there are two asks wearing one name. Replacing the body map is a fix to a screen Greg thinks is
broken, and it is not a treatment plan feature. Generated imagery on the plan is the part with no job
yet.

Your objection, 1:37:00, went unrebutted: *"if we directly replace the 3d body map in our app right now,
it's really risky because everybody might generate different kind of images, and the images will take
over the full screen... we don't have any control of the outcome."* Your counter, which nobody argued
with: a documentation / images section under each Health Hub category, so a generated condition map files
under the condition and a procedure diagram under procedures.

Jay's bridge if it must touch the plan, 1:34:45: *"if the goals refer to a condition or procedure, then
we can say generate an image for this specific goal... If because you have broken ribs, you can do ab
exercises or something like that. Then choose the broken ribs. That's what Greg wants."*

Kelly's alternative home for it, 1:34:13: the look-good-feel-good photo comparison. *"take a picture,
feel better."*

#### "Supplement research, not a supplement list"

Greg, 9/1 at 0:38:47 to 0:43:33. This is not a list item, it is three capabilities:

1. **Label photo to verdict** — *"I just take a picture that's on the site, or if I was dumb enough to
   buy it, and show the front and then I show the ingredients. It tells me immediately whether it's
   bullshit, whether it's over tested, any third-party review."*
2. **Per-ingredient interaction check** against current meds — *"it looks at each individual ingredient
   and says that one has a known capability, this one can be dangerous to you... based on what you're
   taking."*
3. **Reverse search** — *"tell me all supplements that are good anti-inflammatory supplements that will
   not interact poorly with the rest of my medications."*

His framing example: *"I don't take anti-inflammatories, even though my CRP is high. I just take
turmeric... but you can't ask Orion that."* And the business ambition behind it: *"eventually we'll get
to a section in our system that recommends supplements that have proven tests done on them... and then
we'll start making a cut on the sale."*

Jay mapped it to backlog item 14, the Orion `+` button for image upload, and proposed the UI as a button
that launches Orion with the image, plus *"suggested questions on the whole medication list."*

**Kelly's scoping note is the one that affects your layout**, 0:39:59: *"I think we left it outside
because users would want to do that whether or not they're using the lifestyle plan. So it's part of it,
but it's not only accessible through the lifestyle plan. It's accessible to any premium user."* Greg
agreed: *"it should be standard feature."* So the entry point lives on the medication list and the plan
links to it. Do not build the plan as the owner of supplement research.

#### "Greg wants ingested recipe / workout content in the one pager or one click off it"

Greg, 0:35:12: *"we're going to have to be prepared to take on new services quickly on this preventative
care. Being able to store videos of workout programs, diet recipes, things other than just say donate
sugar and workout... Pick a popular recipe program and figure out how to grab that data and ingest it
and make it available in that one pager, or click off that one pager."*

Also in that stretch, three things he did not want dropped, 0:34:57: *"Let's not forget about that
translations, the radiology reports and the image generated."*

And the frame he keeps returning to, 0:40:25: *"the problem right now is that we got to do everything
necessary to keep them from going to ChatGPT to work on their health. And that's a huge one."* That is
the argument for spending real effort on this screen rather than shipping a list.

#### "Med adherence + goals get built first"

Jay, 0:55:53: *"without medication adherence and goals, you can't really create a treatment plan, so
those come first."* Kelly's framing for Greg, 0:57:13: *"when we say the treatment plan will be done,
we're not like will be the first thing we work on. It's the elements that go into the treatment plan that
are actually being developed first."*

Jay also raised a resourcing fork nobody closed, 0:55:53: *"I guess we'll have to ask him to pick between
caregiver and treatment plan."* Greg's 9/1 answer was implicit rather than stated: *"Yuehui get past this
and get on with the one I want, which is the goal and lifestyle plan."* Your own line in the weekly put
caregiver implementation after the treatment plan first version, at lower priority. So it is decided in
practice and never decided out loud.

#### "$599 per-plan provider fee came off the order form"

Kelly had it as "lifestyle treatment plan selected by practice user", a flat rate per patient the
provider activated it for. Greg killed it live, 1:11:08 to 1:11:59: *"Why is that on his order form?"* ...
*"That disincents him from turning on patients."* Kelly: *"Let me take this out then."* The patient
premium requirement stays.

The acceptance criterion he gave you at the end of the 9/1 walkthrough is worth pinning above the
mockup: *"This software is going to be a whole lot easier to sell if we can prove that they can, with
little work on their side, make more money."* The plan's job in his head is to prove provider revenue
with minimal provider effort. Judge every screen against that sentence.

#### "Billing codes still unverified"

Greg, 1:12:08: *"Have you confirmed that we he could actually charge for the preventative plan?"*

Kelly's status: obesity and weight management look billable by a physician or clinical staff with no
special credentials; diabetes education requires a registered dietitian; assessment and nutrition codes
are probably already being billed so they come off the list; prevention counseling codes she is still
adding. Greg's filter: *"look at those that we don't believe he's billing. It does not require him to be
a licensed dietitian."*

This gates the provider-review half of the feature, which is why Jay's don't-overbuild rule exists. It
does not gate the Orion-drafted half.

#### "Billing needs 'preventative', every 9/1 mention was 'lifestyle plan'"

The 8/24 requirement was that the name carry "preventative" so it maps to a billable service. Every
mention across both 9/1 calls was "lifestyle plan" or "lifestyle treatment plan", and Greg used
"preventative plan" only when asking whether it could be billed. The name is still open, and it is now
carrying two jobs: what the patient sees, and what the claim says.

---

### From the 9/15 design review with Kelly

Source: **Design Review, Tue 2026-09-15, 47m.** Kelly and Yuehui only — Jay's internet went down.
Yuehui walked the updated user flow and the first plan wireframes. Kelly's verdict on the flow was
*"yeah, that looks really good"* and on the wireframes *"this looks great"*, then she gave three asks,
which she summarised herself at the end: *"conditions, base status functionality for premium
upgrades, and then messaging. I think those are the three big things."*

#### "Call out the active conditions on the plan"

This is the sign-off gate from 9/8 restated. Kelly: *"I think we need to call out the two active
conditions a bit more clearly because Greg did really highlight that. And people want to improve based
on conditions, right? So are they diabetic? Are they obese? Are they managing cancer?"* Her follow-on
is the design consequence: condition specificity is what lets the plan pull real detail out of the
record — *"if it's a specific condition, there's going to be specific treatment plan details, and
you'll want to make sure it's clear that those are incorporated into the meds, diet, exercise
categories that you already have."*

Yuehui's constraint against duplicating it: *"provider still we have the widget of the active
condition... I don't want to have the redundant information on their dashboard."* Her answer, which
Kelly accepted: *"probably do one paragraph of the reasoning, but have some, we have the source chip,
so they can hover and see the conditions."* Kelly asked for at least a placeholder on the provider
view before the Greg meeting: *"you may want to add a placeholder here that says the conditions above
med sleep activity nutrition, just so he knows that we're including the conditions up there."*

Kelly also floated linking those conditions through to the conditions tab. Not decided.

#### "Show where the plan came from"

Kelly wants the provenance to be more than "Orion said so": *"not just Orion but that it came from
your doctor or medical plan already"*, and for Orion's own contribution, *"that'll be national
evidence from you know prevention task force or some condition specific treatment."* So three source
classes on the reasoning: medical record, provider clinical note or existing treatment plan, and
Orion's clinical evidence. Yuehui's framing: the user should be able to *"review the reason and to
think about better they need to change or further editing."*

#### "Put the patient's stated goal in the plan"

Kelly's addition, and the most open-ended one. Examples she gave: *"I want to lose weight... I want to
be able to pick up my grandkids... I want to walk without wheezing... I'm an elite athlete and I want
to run a five minute mile."* Two consequences she named: it feeds Orion's drafting, and *"that should
also go into automatically the notes for any visit to their doctor."*

Yuehui pushed back on how the goal gets captured, and this is worth keeping: *"I don't want Orion to
initiate the treatment like a traditional wellness app where they let the user do a questionnaire and
set the goals for them. I don't want that way because we are the AI native app."* Orion drafts first,
the user refines in conversation.

The hard case Kelly raised is a goal that is clinically wrong. Her example: an obese patient whose
goal is *"I want to play with my grandkids"* or *"my knee hurts"* rather than weight loss, where Orion
has to curate the underlying goal from the stated outcome. Yuehui's inverse case: a patient already
at an unhealthy weight who still asks to lose more, where Orion *"can stand in and tell the user
probably it's not an ideal goal for you"* and route to the doctor. Both need Orion to ask about
current physical ability and limits, which Kelly conceded *"might be a later phase."*

#### "List what a base patient actually gets, category by category"

Kelly's worry is that base access undercuts the premium story: *"they may get to see it but they may
have to unlock it... to actually use it on the patient side, especially with any Orion questions and
diet recipes and the details behind it, that in my mind requires a premium status."* She also warned
this may not be stable: *"be prepared for Greg to maybe change his mind."*

The per-category cut Yuehui proposed in the room:

- **Meds** — adherence logging stays. One-click daily log, no Orion capability needed. Orion's
  suggestions and med recommendations go away.
- **Sleep** — tracking stays, shown against the provider's target. *"There's no reason we just block
  them from there."*
- **Activity** — same as sleep.
- **Nutrition** — manual logging stays. Recipes go. Photo recognition of a meal is premium. A recipe
  or diet plan the provider specified still shows, but read-only.

Upgrade hooks: dismissible and first-time only. Kelly: *"they could click off and dismiss, but if the
recommendation came up as a premium upgrade, they could just close it... so it's not a constant
bombardment of premium recommendations."* The later version of the hook is meal-service partners
(Purple Carrot, Hungry Root), which is parked.

#### "Message your doctor instead of a dead-end lock"

Today's flow ends a locked plan with Orion saying editing isn't allowed, contact your provider. Kelly
wants that turned into an action: *"instead of just confirm the plan or saying this plan is locked and
you can't edit it till you see your doctor again... that would be not the plan is locked, but message
your doctor about."* The payload matters as much as the button — *"the doctor, in their view, has all
the source information and questioning that the patient did with Orion already, so the doctor doesn't
have to look it up."* This depends on the patient–provider messaging that Jay may build himself
(see Provider — Patient).

#### "Decide the labs row"

The one open disagreement. Kelly wants labs as a **separate row**, reasoning that *"a screening is a
prevention measure. A lab is a treatment status"* — if you're diabetic on insulin, one of the plan's
goals is getting A1C back in range, and that belongs in the plan rather than only in Inside Health.
She was direct about wanting it in the first pass: *"I would default to at least include a labs row to
know that we're thinking about it... I'm going to say try to include it."*

Yuehui's counter is to hold at six categories and surface out-of-range results through the conditions
reasoning instead: *"let me think about because the treatment plan will add the current condition and
the reasoning behind that, so probably I can pick the lab result really close to your active
condition."* She left it as *"probably it just can be the seventh category. Let me think about it."*

Both agreed on the filter regardless of where it lands: Orion picks which labs belong to the condition
(*"the doctors said you have diabetes. Which of these labs should be monitored? And Orion should be
able to pick those, like your A1C and glucose"*), and they only appear while out of range. Kelly's own
counter-example for why a raw out-of-range list is wrong: *"I had a bunch that were abnormal or out of
range, but the doctor and Orion were like, meh, they're just low... I wouldn't want all those to flag
on my treatment plan."*

#### "Work through initiation and onboarding"

Kelly's list of scenarios, which Yuehui acknowledged as the missing half — *"right now I just create
happy paths"*:

- Where does the health goal get captured if not in onboarding? *"Do we need to add an onboarding or a
  profile question to say what are your health goals?"* A "none" answer defaults to maintain current
  status.
- What kicks the plan off if the patient never connects a record, or connects only Apple Health?
  *"They wouldn't have a treatment plan. Would they have one just saying I want to lose weight?"*
- How much input is enough — is one medical record sufficient to generate?

Kelly expects Jay to have a parallel list from the dev side.

#### "Premium patient edits the draft with Orion until the provider pushes it"

**This contradicts a decision already in the list.** The 9/11 team meeting settled *"v1 has no patient
editing at all, not even premium; the patient sees the plan and their progress, the provider is the
only editor."* The flow presented on 9/15 has the premium patient editing freely with Orion — target
values, goals, re-drafting on request — right up until a provider reviews and pushes, at which point
it locks. Kelly did not flag the conflict and reviewed the flow as shown.

Both can't be true in v1. Either the 9/11 line is superseded, or the flow going to Greg overstates what
gets built. Worth resolving before the Greg review, because it changes the disclaimer states too: the
9/15 flow has "generated by Orion, double check with your provider" before push and "reviewed by your
doctor" after.

#### "Six categories map into care and lifestyle"

Yuehui's summary of what she and Jay agreed, restating the 9/11 vitality sync: meds, screenings and
vaccines land under **care**; sleep, activity and nutrition land under **lifestyle**; the plan's goals
become the sub-goals of those categories, and both feed the vitality evaluation.

#### "Multi-plan for a patient with several conditions"

Kelly talking out loud, explicitly not for now: *"they might want two different plans. So we're going
to have to think about what that looks like... I think this is fine for now, but we may need to be
prepared to make it a multi-plan."* Yuehui agreed the six categories won't carry a comprehensive plan
forever, *"but let's start from here."*

#### "Show Greg the flow and get the approval"

Kelly's closing push, and the reason the conditions work is urgent: *"we just need him to approve it so
we can move forward with dev. Because last time he didn't approve it, right? He needed conditions.
That's why I'm really focused on this condition piece."* Yuehui's plan was to review the user flow
with him and show the wireframes only if he asks, since they're still low fidelity.

---

## Prototype — Claude design

Added 2026-08-11. This restates and sharpens a line from the old manual list that I wrongly dropped
as completed: *"Build the json file as a real-patient-like profile that can be read by Provider and
Patient app; build the patient app prototype on the Claude design, check Demo session's Kelly's user
flow to see the involved screens."* Same workstream, now split into a parent and a ghost task.

### "Build the mobile patient app in the Claude design prototype, from the Figma screens"

The parent. Rebuild the patient app as a working prototype in the Claude design environment, with
screens sourced from the Figma file rather than redrawn.

- **Scope the screens first.** The old note says it: check the Demo session's Kelly user flow to see
  which screens are actually involved. Build that set, not the whole app.
- **Capture route.** There's already a process for this in the folder — `Claude - Figma Screen
  Capture Playbook.md`, `Figma Capture — Quick Start (Humans).md`, and `figma-match-check.html` for
  verifying the prototype matches the source frames.
- **Why it matters.** It gives the provider prototype a real patient-side counterpart, so
  provider ↔ patient behavior can be demoed end to end instead of described.

Existing patient-side prototypes in the folder that may feed this: `Dashboard Testing/`,
`DailyHealthTracker/`, `OrionVoiceMode/`.

### "⇢ parallel — build the json file to mock the live sync between provider app and patient app"

**A ghost task, not a sub-task.** It runs alongside the parent: it doesn't wait for the patient app
prototype to exist, and it doesn't pause when the parent pauses. That's the distinction — a sub-task
rides along with its parent's status, a ghost task keeps its own.

One real-patient-like profile JSON that both the Provider app and the Patient app read, so a change
on one side shows up on the other without a backend. That's the "live sync" being mocked.

Open questions to settle while building it:

- **Shape** — one file, or split per domain (meds, labs, conditions, wellness)?
- **Who writes** — in the mock, does the provider side write and the patient side read, or both?
- **How the sync is simulated** — shared in-memory state, polling a file, a fake event?
- **What has to round-trip** — meds and adherence, verification / correction state, data groups
  pushed from the provider side, Orion's view of the same record.

It should use the same category vocabulary as the rest of the system — see the LOINC category
mapping (7 real categories, ~20 defects in the source file) and the full-data column inventory
under B2B, even though that one is paused. If the JSON invents its own field names, the full-data
tab and the prototype will drift apart.


### "Build the caregiver screens as a clickable prototype"

Added 2026-08-25. Distinct from the parent line above — this one is caregiver-only and driven by a
specific need she named at the end of the design review: *"I'm also planning to build the prototype
on the cloud design, so we can have a better review of the Caregiver's screens… there's a lot of new
entry points, so I need to check every button or interaction is correct."* Kelly's reaction: *"Oh,
nice. Yeah, that's cool."*

The point is interaction verification, not visual fidelity. The caregiver work has added entry points
in several places at once — network tab, homepage add button, connected-person dashboard, access
management, the two request flows, the mode banner on half a dozen screens — and a static set of
frames can't show whether they all connect. This is also the artifact Greg walks through on Tuesday.

---

## B2B — Provider Dashboard

Source: same 2026-08-07 meeting.

**Status as of 2026-08-10: paused.** The 8/7 meeting gave the "Full data sort & Filter columns" line
a concrete deliverable (the Excel tab), which briefly un-paused it — Yuehui has since put it back
on hold: not the priority right now. Caregiver is the live block. The three lines below are
sub-tasks of the Excel tab and are paused with it; they're nested under it in the short list so the
pause reads as covering the group. The spec below is kept intact so it can be picked up as-is.

### "Full data sort & filter columns -> new tab in the logic / code Excel..."

Deliverable is a **new tab in the existing logic / code Excel workbook** (Kelly's), not a separate
doc. It should be the one source of truth for full-data mode in the provider app, enumerating:

- every category (conditions, medications, labs, etc.)
- every table within each category
- every column in each table
- per column: does it support **sort**, **filter**, or **both** — and *how* (what the sort order
  means, what the filter operates on)

Ties to prior full-data decisions already recorded: the three-tier sort model and what a user sort
may/may not override; select mode carried in the sticky header with one expand, never a stepper;
the per-row "+" split and the rule that a lens filters but never arms a push. Those are behavioral
rules — this tab is the column-level inventory underneath them.

### "Map each element to a category from Kelly's Excel where it fits; flag the ones that don't"

Best-effort mapping, imperfect is acceptable. The value is in the exceptions: anything that doesn't
map cleanly gets flagged so special rules can be defined later. Related known issue: the LOINC
category source file has 7 real categories, needs 2 columns for the UI, and has ~20 defects
already catalogued — check that before assuming a category list is clean.

### "Small UI snippets per column -> how sort shows (arrow), how filter is picked"

Small visuals, not full screens. Per table/column: what the sort control looks like (up/down
arrow state) and what the filter affordance is — chips, dropdown, text search, range, etc.

### "Link the snippets to the rows so Jay and Kelly can review in one place"

Attach or link each visual to its corresponding row/column in the Excel tab. The point is
reviewability: Jay and Kelly should be able to read a row and see the intended control without
hunting through a separate file.
### 9/4 additions — team meeting Fri **2026-09-04**

The 8/7 full-data block above stays paused. Everything below is new, and two of it is **Next** —
provider-side design is live again because Dr. Portu's pilot starts against this UI.

Framing that governs all of it, from Jayanth: *"these are changes good enough for at least Dr. Portu
to give it a try during the pilot and give us some feedback on what is a must, what is not… I think
we need to prioritize this feedback also. Like, what is something that you can't live without versus
what is a nice to have. And then we can start acting on what you can't live without."* Kelly folded
that into the Portu statement of work as a formal testing protocol, so pilot feedback is the
tie-breaker on most of these.

### "Show the provider what the patient is and isn't sharing"

Jayanth raised the gap; Kelly assigned it. His version: *"we will have to share the same thing with
the provider also somehow, on what the patient is sharing. So that maybe we might have to think
about the UI for that. Like, how do we show the provider what the patient is sharing and not
sharing?"* Kelly: *"based on the demos, the providers are gonna want to see this"* and then the
assignment: *"so UHI will need to add that to the provider like phase two or three feature
updates."*

Why it's urgent for her: she has been telling providers the wrong thing. *"we've already gotten
questions, and actually I've been saying it wrong… I said you'd have access to a DEXA scan or a bio
report or an image or whatever. So I didn't realize."*

**Jayanth split it into two design problems and it should stay split:** *"that's two things, right?
One, document center in provider UI — that's its own UI update. Then there is, what is the patient
sharing UI in the provider UI also. So two things we might have to figure out."* The first is the
next entry; this line is the second — the sharing state itself, which is the provider-side mirror of
the patient permission screen.

### "Providers want the actual source document, not the extracted care plan"

Kelly, twice, and the second time with a count: *"It's been more than one provider that really wants
to see the actual document. I need to see the source"*, and *"I know we'll need it, UHI, because
pretty much every demo I've done, at least the last couple weeks, they wanted to see the documents…
they want to see the actual document, whether it's pulled from the health system or something the
patient uploaded."*

The gap she is describing: the provider can ask Orion for a care plan and get the extracted content,
but cannot reach the document it came from. *"you're bringing it in from the actual code versus a
picture of a document in a CCDA structure… maybe we have to think through that, Yuehi, from a UI
perspective down the road."*

Partly addressed already, which is why this is a design pass and not a new feature: Jayanth's Orion
answers now expose sources — *"if you click on documentation it shows the document sources, click on
that and see"* and *"It shows the excerpt that was used to answer that question, and then if you
click on View Document, it'll show the actual document also."* But *"the citations part is not
completely built out yet"* (see the inline-citations note below). On the patient side the Library is
what she demos; the provider has no equivalent. Related work:
`orion-source-peek-panel-wireframes.html`, `orion-source-types-wireframes-v1.html`,
`source-display-patterns-ai-products.html`.

**Also outstanding against Yuehui's existing spec:** inline citations. Jayanth: *"I know Yue had
inline citations in her UI. That part is not fully built out yet… initially I want to bring in inline
citations for web search sources."* And the current state: *"you see those dangling markers on top,
like where it says five in the answer. Those need to be actual links… you will see those numbers, but
they might not map to anything yet."* Nothing new to design; it's a build-completeness gap worth
tracking because demos show it.

### "Patient updates color coding"

Jayanth's flag, addressed straight to Yuehui: *"each one of them has a different color code, right?
The medication change has a different color code, allergy change has a different color code,
condition has a different color code, on all the patient updates. I don't know if you want to think
through that."* He extended the per-category colours to conditions and allergies while removing meds
from the timeline, then realised the pattern was inconsistent.

Yuehui's call, which stood unchallenged: *"I think if in the patient updates we mix cross categories,
probably I will just remove the color coding for the patient updates."*

**Kelly's caveat is the thing to watch.** The original intent was priority, not category: *"initially
the patient updates was red because we were thinking maybe it needed to stand out to the providers.
Like, pay attention to this, because this is what your patient changed."* And: *"otherwise, there's
nothing like red in here as like a priority thing."* So removing colour removes the only urgency
signal on the provider dashboard. Either something else carries urgency, or this comes back after
pilot feedback. Check against status tokens either way — green already means in range, and Jayanth
separately wants *"bright green"* for provider-reviewed plans.

### "No detail view anywhere in the provider UI except reports"

Jayanth, thinking out loud while deciding where diagnostic reports land: *"reports has a detail view,
right? It always has a detail view. We don't have a detail view for any of the components right now
in provider UI, which they might start asking for. So that's another thing that we'll have to keep
thinking about. Like, where does the detail view land?"* And on observations specifically: *"you can
click through the observation data to go into observation detail also. That I think is needed."*

Yuehui's answer, accepted: *"for the documentation, we can just use the document reviewer, that kind
of component. But the data detail — I know that even on our mobile app right now, we didn't finish
the detail page for the single data."* So the pattern is half-solved on documents and unsolved on
single data values, on both platforms. Doing it once for both is the opportunity here. Related:
`provider-detail.html`, `data-verification-prototype.html`.

### "Category column on the provider labs table"

Yuehui's own ask, agreed in the meeting. Jayanth had brought the patient-side lab groupings into the
provider UI as filters: *"the same categories that we have on the patient side, I had these as
grouping filters. You didn't have this in UI, but I think this makes sense, because if the provider
says I don't know why metabolism includes A1C, that gives us enough feedback to say okay, maybe we
should change this on the patient side also."*

Yuehui: *"is it possible to add one column for the labs and call it the category, so they can have
some mapping?"* — clarified as *"the column is just a reference to this sub tab."* Jayanth: *"Yeah,
we can add a column also, but I thought this was simpler."* → *"Perfect."*

The reason it matters beyond the provider table: the groupings are the same on both sides, so
provider feedback is free validation of the patient-side categories. Jayanth: *"I included these so
that we can map any feedback from provider and update it on the patient side also, so that we are in
sync."* This is the LOINC crosswalk showing up again.

### "Suggested question pills: Kelly wants one click, I want the review step"

A design decision that was challenged and held. Kelly: *"I like that these are here, but it takes a
lot of space of the answer, and then now the pills make me click it twice, right? I had to click this
and then hit send to Orion. Is this a UI thing that Yuehui can work on?"*

Jayanth defended the behaviour first: *"that was the idea, right? Because we are not showing the full
question, we are showing half the question. So if you click it, you show the full question. How do
they know the full question if they don't?"* Then Yuehui gave the real rationale: *"I want the user
to at least check and review the question they want, and also they can add more information if they
want. So it's not one click to send the question."* This is the fill-don't-send decision already on
record for Orion chips.

Kelly accepted a test rather than a redesign: *"we'll just test it. So when I'm creating the
statement of work with the test components, we'll add these types of details for feedback from
Portu."* Her residual concern is space, not clicks: *"it's just hard when we get a long answer…
there's just not a lot of space for it."*

**Blocked on Portu feedback.** Don't pre-emptively redesign it. The space half is being handled by
Jayanth's chat-box width change: Yuehui asked *"can we make the Orion chat box a little bit wider?
Then the pills will not just be in one vertical line, it can be the horizontal layout, so we'll
release more space for the text"* — he agreed, *"I can increase the size of the width."* Web only;
Kelly confirmed *"this is only on web currently, right, Jay? So we don't have to worry about a mobile
layout."*

### "Diagnostic reports land in Full Data for now"

Jayanth's interim placement, decided in the meeting and shipped the same day: *"that's the only one
that I think I'll add today before I release it to production"* and *"I'll just keep it in the full
data for now, and we'll see if there is another way to get through it."* Also carried the meeting's
other provider-side changes: meds removed from the dashboard timeline (*"we haven't decided on what
we will show on meds here, so I removed the meds here"*), and the meds category swapped for out-of-
range labs to match the patient side.

Nothing to design yet — it's the fact to design against, and the reason the detail-view question
above came up.



---

## B2B — Healthcare Monitor (employer)

Source: **C4P team weekly, Tue 2026-09-15**, roughly 0:37 to 1:02. Greg's ask, new this week, and the
only genuinely new design workstream out of either meeting.

Full extraction, with the strategic frame and the constraints, lives in
`C4P_MonitoringEmployerPlatform_Requirements-Brief_v1.md`.

### "Quick mockup of the aggregate employer view"

Greg's business case first, because the design follows from it. An employer running a preventative
program wants to prove it works so they can negotiate insurance rates: *"I'm running these preventative
programs. I'm going to have healthier employees. They're going to have less sick time, but most
importantly, I'm going to drive down the amount of disease coming out of my installed base, I'm going
to use that to negotiate down my rates for the insurance companies."* The market argument is that it
opens C4P to *"every large employee base in the country"* rather than one doctor at a time.

The starting point is an existing asset, not a blank page. Kelly: *"you did a mock for us when we went
to Indiana, and it was basically saying all your patients, how many are in the needs focus versus
stable, and then you drill down based on conditions. So the group level analytics, basically, for the
patients in your population."* Part of that (the employee network view) Jay actually built; the health
summary half stayed a mock.

What Greg wants in it:

- **Aggregate only, anonymised.** *"You don't have a HIPAA agreement to look at an individual, so it's
  anonymised data that's aggregated, and they don't really want to look at every individual. They want
  to look at how am I trending."* A 100,000-employee HR department has no use for a patient list.
- **Goals on top, compliance on the bottom.** *"You'd want the goal side on the top, and on the bottom
  you would want the compliance side. How many of my patients are actually following their diet, or
  how many employees are following the diet, doing the workout programs, taking their meds."*
- **Configurable, like the provider dashboard.** *"I would even use the framework you did for the
  provider, where it's user-defined dashboard. Let them pull in what the metrics are that they want."*
  His metric examples: glucose trending pre-diabetic, A1C, LDL and the statin side, skeletal problems
  and recent breaks, smoking.
- **Segmentation.** *"Show it to me for all men. Show it to me, all women. Show it to me for 35 years
  old and below... Show it to me by state."* Kelly added conditions and geography.
- **A new role.** *"It's a new role called call it health administrator or health monitor."* Yuehui's
  read, which Greg confirmed: a standalone desktop app for the employer, not a view inside the provider
  product. Her scoping question, also confirmed: *"their role is basically just monitoring, right? The
  treatment plan still from our concept is from the patient and the provider, but the employer, they're
  just monitoring their status or adherence."*
- **Jay's half.** Dynamic query generation off whatever metrics get configured. Jay's view is that this
  is the same concept as the employee-network work already started.

Greg also wants a tier above the employer eventually — *"I just want all the data, which we would start
selling to the government and pharmaceutical companies"* — which is parked. Kelly noted the same
aggregate-query capability is something providers will want for their own panels, and Greg flagged
clinical trial recruitment as a third use.

Fidelity expectation is low and Greg said so: *"I'd even tell him this is an alpha stage right now...
but I have to have something to show."* Yuehui's estimate: *"if it's a mock-up or the quick prototype
based on our last version, it should be quick, but I can integrate all the ideas we have. On the UI or
the products, it probably is not the polished version."*

### "Greg's order is treatment plan wireframes first, then this"

Kelly asked the priority question directly: *"do you want her to finish the prevention treatment
wireframes to get to Jay for development first, or you want her to take a few hours to get you
something first?"* Greg's answer: *"he's got to get the product built first"*, so the order is treatment
plan → hand to Jay → monitor mockup.

The order and the deadline don't reconcile, and that is the thing to watch. Greg also said *"take a
shot at it, and then buzz me as soon as you got something to look at"*, and his Lisa meeting is
**Wed 9/23**. Kelly's own estimate was *"I'm just not sure how much can be mocked up with Porto and
other things going on by next Wednesday... maybe by Friday"*, which lands after the meeting. Greg
believes the treatment plan is already handed off (*"you've got enough UIs for Jay to start on now"*),
and Yuehui corrected him in the room: *"the treatment plan, no, it's not ready for Jay for now."*

Kelly's priority stack at the end of the weekly put CareCloud first, the healthcare monitor second, and
noted this pushes down caregiver features, image inclusion and partner functionality again.

### "HIPAA arrangement is unresolved"

Greg's assumption is that a HIPAA-compliant form between the health monitor and the employee solves it.
Kelly's objection: *"who's the covered entity in that situation? ... A provider is the covered entity"*,
and an employer isn't one. Greg's counter is that the employer could be the provider of the preventative
portion while each doctor provides the medical portion. Kelly: *"I've never heard of that, but yeah,
interesting idea."*

Where it landed, roughly: HIPAA consent is probably the wrong instrument, the employer likely already
has personal-data consent from employment, and the real exposure is *"what potential laws might you
break with any perceived bias or undue consent."* Kelly took the research. This doesn't block the mock,
but it does gate anything that shows employee-level opt-in or incentive mechanics, which Greg raised
(*"the employer could offer an incentive that says I give you 50 bucks a month off of your payment, but
you have to allow us to see whether or not you're doing a preventative program"*).
### Build order for the 9/23 mock

Five sub-tasks under the mockup line, in order. The cut is in §8 of the brief. The point of the mock is
to make the aggregate idea concrete enough for Lisa to react to and to invite her to shape it, not to
be production UI.

1. **One desktop screen, one fictional employer, one configured metric set.** Not a metric picker
   working end to end, not multiple employers. Greg has already accepted alpha fidelity.
2. **Two-half layout.** Outcomes on top, compliance on the bottom, exactly as Greg described it. The
   causal claim the screen has to carry is that the diet and workout programs move the numbers above.
3. **A filter bar that visibly does something.** Draw at least one filtered state, not just the
   control. Greg's demo script is a sequence of filter asks — all men, all women, under 35, by state —
   so the filtered view is the thing he will actually show.
4. **A suppressed cell in the filtered state.** Below a minimum count the cell reads *too few to
   report* instead of a number. This is the answer to the re-identification problem in §6.2 of the
   brief: three stacked filters routinely produce a cell of one or two people, and an HR director knows
   who that person is. Putting it on screen turns a liability into a trust signal, and it is much
   cheaper to design now than to retrofit, because it changes how every tile behaves when filtered.
   Nobody raised this in the meeting — it is a recommendation, not a decision.
5. **Metric picker as a panel.** Drawn, not functional. Enough to show that the administrator chooses
   what they track, which is the part Greg keeps returning to.

Deliberately out: the second aggregate tier, the provider version, trial recruitment, incentive
mechanics, and roster onboarding. The roster question is the real unknown (§7 of the brief) — an
employer's headcount and C4P's enrolled patients are different numbers, and which one is the
denominator changes the story every tile tells.

---

## Provider — Patient

### "Prescription refills -> a requirement for replacing a portal"

New on 9/1, and it arrived attached to a deal. Greg's prospect wants to drop his portal vendor and use
C4P instead: *"his ultimate plan is he'd like to replace his portal with us"*, and *"he says 70% of his
patients use the portal, so that should get us much higher conversion rate to premium."*

Greg, 0:14:44: *"If we're going to start replacing portals, we have to be able to refill
prescriptions."* Kelly added it to the functionality list. Her constraint, same shape as appointments:
*"we're connected to a partner, we can add anything that they send us, but we don't have that"* today.

So it is a partner-data dependency before it is a screen. Nothing to design until Jay says the data can
come in.

### "Jay may build the minimal patient–provider messaging himself -> stay aligned, don't block on it"

Priority call from the meeting: messaging is Jay's to build if he wants it; Yuehui's focus stays on
caregiver UX. The only obligation is alignment — see the caregiver messaging-anticipation line.
### 9/4 addition — team meeting Fri **2026-09-04**

### "Base patient access lasts as long as the provider contract, not 90 days"

A rule change with UI consequences. Kelly settled it in the meeting: *"I would just say that the
patient's base access lasts as long as the provider's contract is in place. That's what we tell
them"*, and the part that touches design: *"they should not need to get another code or refresh
it."*

So the 90-day expiry states go away, and with them any copy about re-entering a code or refreshing
access. What replaces them is an edge case nobody has designed: what a patient sees if the provider's
contract ends. Check the paywall and trial screens for stale expiry language
(`paywall-trial-ended-wireframe.html`, `orion-free-tier.html`, `invite-access-flows-v1-v2.html`).
### 9/8 addition — team meeting **2026-09-08**

### "Add picture / attach file in the chat box"

Greg's framing is competitive, not incremental: *"if anybody else runs into anything else you can do
in ChatGPT you can't do in Orion, you need to bring that up. If they have to leave our system to go
to ChatGPT, it's never going to work."* The specific failure: *"Orion couldn't tell me whether this
particular mental clarity drug worked. ChatGPT took a picture of it and immediately told me what all
the ingredients were and which ones were useful, which ones weren't."*

Jay identified it as backlog item 15, *"take a picture of supplement"* — the same item the supplement
research feature maps to. Kelly: *"Yuehui might need to take a look at that with Jay and make sure the
feature works on mobile for patients."* Yuehui: *"I have an old design with the add button or other
stuff you can add in this chat box, but I can review that and probably we need to upgrade that."*

**Scope note:** Greg does not want a button for its own sake — *"I don't even know if you need to make
it a button. All you do on ChatGPT is you just copy the picture and put it in the question bar."*
On mobile that means camera / photo / file from the composer, not a separate flow. Greg put the
alternative-medicine commerce idea behind it as *"a dot one release after you get the base system
out"*, and Kelly marked the whole thing *"a next priority for now."*



---

## Meds — add, schedule, log, tracking

Carried from the manual list (Sept 2025 onward), still open.

### "Make the FHIR code and the user-end input mapping."

Map FHIR `Timing` structures to what the user actually types/taps. The manual list has a worked
diagram covering: `Timing.repeat` in three groups of fields (how often — frequency/period/periodUnit;
when — timeOfDay/dayOfWeek/offset, semantic code + set time; how long — bounds[x]/count/duration),
plus `Timing.code` as shorthand (BID/TID/QD/QOD/Q4H/Q8H). Two coding systems:

- **Clock-anchored** — MORN / NOON / AFT / EVE / NIGHT / PHS, abstract parts of the day, each
  defined as "exact time unspecified, established by institution convention or patient
  interpretation". C4P's morning / noon / evening groups map here, with auto-mapping from the exact
  time to the clock-anchored code.
- **Event-anchored** (HL7 v3 TimingEvent, relative to an event) — sleep: WAKE (on waking), HS (at
  bedtime); meals as a grammar, not a flat list: prefix = relation (A/P/I = after/post/before-ish),
  suffix = which meal (C cibus/meal, M matutinus/morning, D diurnus/midday, V vespertinus/evening),
  giving C/CM/CD/CV, AC/ACM/ACD/ACV, PC/PCM/PCD/PCV, IC/ICM/ICD/ICV.

Related files in this folder: `schedule-picker-spec.html`, `adherence-window-labeling.html`.

### "Celebration animation -> try the full screen design"

Existing explorations: `day-celebration-explorations.html`, `day-closes-check-polish.html`,
`day-complete-illustration-layout.html`, `log-all-motion-spec.html`. The open move is the
full-screen variant rather than the inline/card celebration.

---

## User Profile

### "Emphasize the health ID / C4P account that user can share with other people.... even maybe combined with the health hub"

Carried verbatim from the manual list. The idea: the C4P account is itself a shareable health
identity, and that might belong in the health hub rather than buried in profile settings. Adjacent
existing work: `share-health-data-mockup.html`, `share-data-v2-v3-compare.html`,
`patient-consent-wireframes.html`.

---

## Dropped from the old manual list (completed / struck through)

Kept only so they aren't re-raised: marketing materials (provider dashboard features for the
website); meds hi-fi version finished and reviewed with the team; log meds illustration; provider
dashboard "Patient Correction" rethink; vitality evaluation system added to provider dashboard,
synced with patient side; Orion's reply source trace-back design; full data mode bulk selection for
manually building data group widgets.

---

## Archive

_(finished items move here with their detail)_
