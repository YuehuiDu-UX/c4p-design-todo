# Design To-Do — Yuehui

Rolling. New tasks go under a section after each meeting. Date tag = which meeting it came from.
Status: Open (no marker) · **Next** · **Doing** · **Pause** · **Blocked** · **Dropped**. `[x]` = done.
`-` under a line = sub-task, rides along with its parent. `⇢ parallel` = ghost task, runs alongside, doesn't wait.
Longer context for any line lives in `Design-TODO-detail.md` — ask Claude, don't fill it in here.
`design-todo.html` is the clickable view of this file.

**9/8 done. Greg did NOT sign off on the plan** — he withheld it for one reason, the provider-facing snapshot. A second review is agreed but undated (Kelly to schedule). Jay's two-week build starts at sign-off, so the revision is the critical path.

**Order decided 9/9: reports tab first, then the plan.** The phased plan of attack is `Design-Roadmap-PreventativePlan-v1.md` — I answer five of the six open questions myself by drawing them instead of waiting. The questions and what I decided are in `Design-Questions-2026-09-08.md`.

Caregiver walkthrough went to Greg on 9/1 and he approved it. Caregiver moved to priority four on 9/8.

**9/11: the plan entry point is settled, and so is the reports grouping.** Orion always generates the plan — the provider generate button is the trigger for a base patient, a premium patient gets one automatically like vitality — and only the provider edits it in v1. Reports group as out of range / new / past with no date rule. Jay builds meds and goals first, health hub after.

---

## Caregiver — Patient App

- Redesign the care recipient view -> not just allergies / meds / conditions / procedures (8/7)
- Add: recent wellness (steps, goals met), labs / vitals + high-level evaluation, ask Orion about their data (8/7)
- Keep it a minimal caregiver dashboard, still inside the patient app (8/7)
- Caregiver with multiple family members -> Network tab as the entry point (8/7)
- Nav model: caregiver's own profile -> care recipient -> back (8/7)
- Quick view vs. log in as that user -> define the UX expectation, engineering decides the tech (8/7)
- Always show whose data is on screen (8/7)
- Future caregiver-specific app / dashboard -> note the idea, don't design it now (8/7) - **Pause**
- Leave room for messaging -> where the caregiver would see threads with provider / patient later (8/7)
- Finish the pop-ups and the screen content -> the framework is already there (8/25) - **Doing**
- Connect People grouping -> highlight group is the people who share with me, separate section for the people I share with (8/25) - **Next**
  - Icon or colour code for the both-ways relationships instead of a third group (8/25)
  - Replace "connected only" with a deactivated / no-longer-sharing section that can be reactivated (8/25)
  - Decide the default count on the network screen -> 4 now, slider or full list when there are more (8/25)
- Source tiles -> we don't get logos from the health systems, today it's the letter avatar (8/25)
- Show health systems the same way as people -> Jay says they get revisited often, not set-and-forget (8/25)
- Connected person dashboard -> decide whether their connected sources show at all (8/25)
- Action-oriented view -> what does Dad need to do today and how do I help, not just what can I see (8/25) - **Next**
- Health Hub category detail list -> better looking item / field card (8/25)
- Show Greg the caregiver UI and flows next Tuesday (8/25) - **Next**
- Practitioner list is cluttered with nurses -> separate primary care from all practitioners, maybe a filter at the top (9/1) - **Next**
- Restore the "whose records am I viewing" banner + an exit / back to my account control (8/31) - **Next**
- "Last update" with the date instead of a status -> red only when a visit happened after the last refresh, gray otherwise (8/31) - **Next**

## Caregiver — Access & Sharing

- Two grants, two buttons -> view only, and act as me (8/25) - **Next**
  - v1 is UI only, no Orion -> add meds goes through Orion today so it can't be first phase (8/25)
  - Premium on both sides -> mark the feature blocked / inactive when the other person is base (8/25)
  - Pick the one-to-three actions dev can actually ship first, expand from there (8/25)
- Locked categories -> the receiver can only request more, never less (8/25)
  - Templated request note, not free text (8/25)
  - Request tracker -> sent on a date, can be withdrawn (8/25)
  - Granted state -> "act as" or "view only" as of a date (8/25)
- Build the sharer's screen for an incoming request -> that's the screen I'm missing (8/25) - **Next**
- Mode indicator -> pop-up when a view-only user hits add / edit, persistent banner in act-as-me (8/25)
- Define when the caregiver can exit caregiver mode and when they can't -> need Jay on the backend (8/25) - **Blocked**
- Orion's perspective in caregiver mode -> "his meds" not "your meds" -> parked, not the first priority (8/25) - **Pause**
- Share my health data selector -> subtitle under every category, no hover on mobile (8/25) - **Next**
  - Icon on the categories that may include sensitive information (8/25)
  - Default everything on + a Select All button (8/25)
  - Disclaimer at the top or bottom of the screen (8/25)
- Research the consent wording -> what do EMR patient portals use when you add a caregiver (8/25) - **Next**
- Notification design -> every change / daily summary / weekly summary, and per-person on-off (8/25)
  - Practices ask for SMS -> phone notification first, direct text sits in future messaging (9/4)
- Standardize every consent / data-sharing list across provider, patient, network, QR and FHIR (8/31) - **Next**
  - Include uploaded documents and wellness data, Select All, all categories default on (8/31)
- HL7 / FHIR observation categories to our user-facing categories -> build the crosswalk and share it (8/31) - **Next**
- Jay's interim permissions rework is a placeholder for my sharing / caregiver design -> Provider Access renamed and moved top-level, new Manage Sharing entry, patient + care team default on and not optional (9/4)
  - Select all / deselect all comes with my caregiver UI update -> he toggled everything on for now (9/4)
  - New patient-facing header "Used by Orion Answers Only" -> diagnostic reports, health system and uploaded documents, care plans, health kits (9/4)

## Data Refresh & Appointments

- Auto-refresh for health systems -> design it for the main app and the caregiver view (8/25) - **Next**
  - Appointment is the trigger for partner systems -> after the visit, refresh and pull the new labs (8/25)
  - Non-partner systems -> notification instead: "how was the appointment, want to refresh?" (8/25)
  - Decide the entry point -> from the health system, or from the data itself (8/25)
- How do we get the user to enter appointments when the provider isn't a partner (8/25)
- Appointment adherence as a Care / prevention element -> annual, mammogram, colonoscopy, flu shot (8/25)
- Bulk invites without an appointments API -> CareCloud has none, worst case is searching patients one at a time (9/4)
  - Kelly wants a quick daily send in the morning -> one at a time is a big dissatisfier, batch cap is 20-25 (9/4)
- Invite email says "your healthcare provider" -> needs the actual provider name (9/4)

## Health Bio & Stats

- Create an abnormal / out-of-range group in stats -> everything outside normal range at the top, separate from the category groups (8/25) - **Next**
  - Duplicates settled 9/11 -> let the out-of-range lab sit in its category group too, least dev work and there is no category filter yet to justify the other way (8/25, 9/11)
  - Projections and trends run on the out-of-range items too, not only the categorised ones (8/25)
  - Link stats and the diagnostic report so an out-of-range value can't be missed on either side (8/25)
- Health Hub as the other home for the abnormal data -> the dashboard of things to look at (8/25)
- Also flag the values trending the wrong way while still in range -> glucose is Greg's example, feeds the plan (8/25)
- Fasting vs. non-fasting glucose gets misclassified so the trend splits -> may need a user edit, Kelly is checking the codes first (9/4) - **Blocked**
- Compact active-records block on the health hub -> the dense one-page version I drew is not readable, show counts and let the button carry them into the tab (9/11) - **Next**
- Decide whether out of range belongs on health bio at all -> if the list runs long it needs a compact form or it does not go there (9/11)
- Merge the confirm-health-bio content into the permanent health bio page -> date of birth, gender, blood type, tobacco; the today's-to-do page is temporary and then disappears (9/11)
  - Height and weight edit in place from the hub, Jay will wire the direct edit -> health bio still has to stay discoverable for everything else on it (9/11)
- Body map comes off the list view -> list is the default, the entry point stays in health bio, the click stays premium (9/11)
- Mini trend graph stays simple, the abnormal-range visualisation goes in the full graph (9/11)
  - Kelly wants every out-of-range point marked as well as the ring on the current one -> full version only (9/11)
- Drop "entered in error" as a user-facing label -> give each item a status tag that means something (9/11)

## Reports

- Check Jay's add-on for Reports -> see what's actually live before designing on top of it (8/25) - **Next**
  - Diagnostic report already carries every lab value on the panel, including the ones stats doesn't show (8/25)
  - Reports tab is being hidden in the provider UI now the initial one is done -> confirm what that means for the patient side (8/25)
- Radiology report is a quick fix and ugly -> needs a design pass (8/25)
- Anatomy visual -> Orion generates a picture of what the radiology report describes, then the plan hangs off it (8/25)
- Surface new and out-of-range labs on the reports tab -> review the tab first, I didn't design it (9/4) - **Next**
  - Settled 9/11: out of range on top, then new, then past -> no date-range rule and no other bucket (9/4, 9/11)
  - Has to beat the patient portal -> "you've got a new test" is the one thing portals do well (9/4)
  - No push for non-partner systems -> the indicator has to carry it without a notification (9/4)
  - Jay is adding observations read-only into Review your records on every refresh (9/4)
  - Map the EMR's "final" status to normal / abnormal in patient language (9/4)
  - A report is a collection -> the lipid panel carries all its observations, an imaging study is one thing (9/4)
  - Renamed 9/11: needs focus becomes out of range on the reports tab -> Jay: needs focus implies a time rule, out of range is just your current value (9/11)
  - Out of range is driven off observation stats -> Jay pulls the diagnostic reports behind whatever is out of range there, no date logic in v1 (9/11)
  - New means it arrived on a refresh -> a first sync is not new, everything else is past reports (9/11)
  - Needs focus keeps the timing, the goal and the treatment plan, and stays with vitality (9/11)
  - Report detail needs a provider-notes line for when we have doctor notes -> my notes is the patient's (9/11)
- Orion generates the image when an imaging report has no picture -> Greg's ask, only MRI / X-ray / CT, patient first, keep it open for the provider (9/4) - **Pause**
  - Nothing to design against yet -> Kelly can't see her own mammogram, Sutner may be the only system sending images (9/4)
- Images as their own class in the UI -> a mammogram shouldn't sit under tests and procedures, Jay says diagnostic report is the right home (9/4) - **Pause**
- Plain-language label on clinical report names -> nobody searches "breast diagnostic bilateral with tomosynthesis", they type mammogram (9/4)
- Document titles are gobbledygook on both sides -> no filename comes from the health systems, provider + type + date may be the label (9/4) - **Pause**
- Reports tab grouping is due next Tuesday to Greg -> Greg: do it first, the pilots need it, and Jay's diagnostic tab is waiting on my UI (9/8) - **Next**


## Treatment Plan / Lifestyle Plan

- Design the first-pass one-page plan view from Vitality data, and recommend where it lives (8/25) - **Next**
  - Where it goes -> settled 8/31: a section inside Vitality, not a fifth chip, a plan doesn't feed the roll-up (8/25)
    - Decided in substance, never ratified -> Jay doesn't care about the label, "it's the data coming from Vitality" (8/31)
  - Both halves: a short text snapshot of what to focus on, plus the goals with live tracking (8/25)
  - Keep the prose short -> show the provider's goal inside the tracker instead of writing a paragraph (8/25)
- "Verified by your provider" tag on individual goals + a filter for the verified ones (8/25) - **Next**
  - Handle the conflict case -> my own goal vs. what the provider set last year (8/25)
- Prevention elements -> trending the wrong way, not only out of range (8/25)
- Provider adjusts Orion's plan -> 5,000 steps not 10,000, 50g protein not 200g on poor kidney function (8/25)
- Revise the Vitality landing page -> needs-focus goes nowhere right now (8/25) - **Next**
- Name it -> lifestyle plan / treatment plan / preventative plan, still unsettled (8/25)
  - Billing needs "preventative", every 9/1 mention was "lifestyle plan" (9/1)
- Multiple plans, one per provider / topic -> plans list with Active and History, single page each (8/31) - **Blocked**
  - Kelly and Jay both argued for one plan on 8/31 -> Greg hasn't seen either version (8/31)
  - Cross-plan focus summary at the top of the plans list -> that's Greg's one place to look (8/31) - **Blocked**
    - Becomes the top of the single plan if one-plan holds (8/31)
  - Unreconciled targets state -> two plans, two numbers, nobody resolved it (8/31)
  - Provider's own words above Orion on the plan page -> the frames have it the other way round (8/31)
  - Scope plan stats to the plan period, not the calendar month, and store the baseline (8/31)
  - Ended plans should say what happened -> that's where before / after lives (8/31)
  - Mark needs a short plan label, a "2 plans" count, and a Mine state (8/31)
- Premium vs. base settled 9/11 -> everyone who has a plan sees it, premium buys the Orion drill-down: recipes, workout programs, any ask (8/25, 9/11)
- Greg's page content, top to bottom: goals, then treatment / diet / workout / meds under each, then the key lab and radiology problems (8/24)
  - Every goal needs a target, a timeline, and a starting point so the trend has a baseline (8/24)
  - Before / after framing -> what's your current, what do you want your after to be (8/24)
  - Drill-down goes to the screens we already have -> Vitality keeps scanning everything, the plan only measures what was agreed (8/24)
- Provider builds the plan on desktop with the dashboard's drag-and-drop framework -> assembled on the fly per patient (8/24)
  - Patient side displays and inputs, doesn't configure -> no dashboard building on mobile in the first release (8/24)
  - Whether the patient ever rearranges their own plan -> closed 9/11, they do not, not in v1 (8/24, 9/11)
  - Kelly's mobile alternative -> select / pin instead of drag and drop (8/24)
  - Patient edits inputs, not layout -> overtaken 9/11, v1 has no patient editing at all; this is the list for later (8/24, 9/11)
  - Symptoms that resolve drop off the plan on their own (8/24)
- Plan gets amended at every visit -> add and subtract items, show what we agreed vs. what you did (8/24)
  - Provider's pre-visit summary of the plan, and a treatment plan link in visit essentials (8/24)
  - Audit trail -> let the doctor see where the patient went with Orion on their own (8/24)
- Share the plan across doctors and specialists, not just primary + patient (8/24)
- Known useful supplements section off the labs -> turmeric, glucosamine, L-arginine (8/24)
  - Show the backing research -> the doctor has to believe them (8/24)
  - Two ways in -> Orion suggests it to the provider, or the provider adds it directly (8/24)
  - Supplement research, not a supplement list -> label photo to verdict, per-ingredient interaction check, reverse search (9/1)
  - Entry point on the medication list, the plan links to it -> any premium user, not gated behind the plan (9/1)
  - Maps to backlog item 14, the Orion + image upload (9/1)
- Diet and workout need real content -> recipes and actual programs, not just "eat less sugar" (8/24)
  - Third-party diet / workout programs adapted to the record -> Greg says get the plan in place first (8/24) - **Pause**
  - Food photo for adherence -> calories, fat, carbs, protein (8/24) - **Pause**
  - Greg wants ingested recipe / workout content in the one pager or one click off it (9/1) - **Pause**
- What I can and cannot do with my condition -> the radiology and physical limits belong in the plan (8/24)
- The plan demo in the auto-onboarding flow -> first thing a bulk-activated patient sees (8/24)
- Scope the first draft to four buckets -> prevention & vaccines, med adherence, diet & nutrition, exercise (8/31) - **Next**
  - Prevention and vaccines -> decide one bucket or two, the recommendation engine already exists (8/31)
  - Diet -> the doctor's order on top, Orion's curation under it, recipes behind a second click (8/31)
  - Exercise -> basics only, link out to PT orders, exercises behind a second click (8/31)
  - Med adherence -> reuse the approved design, don't redraw it (8/31)
- Add sleep as a bucket -> Greg: sleep is part of the base plan (9/1) - **Next**
- Buckets have to be configurable -> Greg wants to add categories later, show a 4-bucket and a 7-bucket state (9/1)
- Stress is out for now -> no data source, Jay can't measure it (8/31) - **Pause**
- Labs as a goal with a cadence -> A1C every three months, doctor-authored, a different shape from the lifestyle buckets (8/31)
- Design the three plan states -> Orion-drafted with a disclaimer, provider reviewed, provider adjusted (8/31) - **Next**
  - Unreviewed is the default state, not the edge case -> every patient with connected data gets a plan (8/31)
  - Jay wants "bright green" for reviewed -> check it against status tokens, green already means in range (8/31)
  - Pre-builder review path -> the patient shows the provider the plan and he updates it by hand (8/31)
  - Draw both frames for Greg -> "your provider built this" vs. "Orion drafted this, unreviewed" (8/31)
- Single plan with the conflict raised inside it -> Kelly: "these doctors need to talk", not a resolution UI (8/31)
  - Keep the per-item provenance mark -> one plan from several providers still says who set each target (8/31)
  - Keep plan history -> amended at every visit means versions still need somewhere to live (8/31)
- No plan number Vitality doesn't also show -> Jay's test, the plan is a projection of Vitality (8/31)
- Entry surface answers "am I on track today" without opening a category -> everything else is one level down (8/31)
- Make it visual and fun -> Kelly wants flashy, dopamine hits, less is more (8/31) - **Next**
- Widget-style composition for the patient plan -> Kelly's second mention, still behind display-only v1 (8/31) - **Pause**
- Configurable med alert with a user-defined tolerance -> "at 2 they didn't take their afternoon meds", not next day (9/1)
  - Goes to the patient and the caregiver both (9/1)
- Image generation needs a job before it needs a design (8/31) - **Pause**
  - Greg's real target is the 3D body map in conditions & procedures, not the plan (8/31)
  - My counter -> a documentation / images section under each Health Hub category (8/31)
  - Jay's bridge -> generate for a goal only when the goal names a condition or procedure (8/31)
- Med adherence + goals get built first -> Jay's next dev tasks, the plan can't exist without them (8/31)
- $599 per-plan provider fee came off the order form -> Greg: it disincents him from turning on patients (9/1)
- Billing codes still unverified -> gates the provider-review half of the feature (9/1) - **Blocked**
### From the 9/8 design review + Greg meeting

**Phase 0 — decide on paper first (9/9):**

- Write the metric contract -> one table, per category, what v1 shows and what it's compared to, this is my answer on evaluation (9/9) - **Next**
- Spec the goal row once -> target, method, provenance, forbidden method, preference tag, current value (9/9) - **Next**
  - Forbidden method has no component today -> Greg's caveman diet case needs one (9/9)
- Draw both plan states -> Orion-drafted unreviewed, and provider-reviewed, so the entry-point question stops blocking me (9/9) - **Next**
- Write the v1 cut line down -> what's deliberately out and what each one waits on, so it stops coming back every meeting (9/9) - **Next**

- Call it the preventative treatment plan -> Greg decided, billing needs the word (9/8)
- Conditions and immediate treatment requirements go on top, above the goals -> Greg: "I've got four alerts: calcium, red blood count, platelets, glucose" (9/8) - **Next**
  - Split known from projected -> "one more lab and I'll be pre-diabetic" is a requirement, not a goal (9/8)
- Provider sets the high-level goals, patient builds the detail with Orion -> mark which tier each row came from (9/8) - **Next**
  - Diet is the model: doctor says lose 10 lbs and rules out the caveman diet, patient picks balanced or low carb (9/8)
  - Patient preferences have to reach the provider at goal creation, not after (9/8)
- Provider snapshot on desktop is the sign-off gate -> Greg withheld sign-off for this and nothing else (9/8) - **Next**
  - One view: known + projected medical requirements, personal goals, out-of-line labs then vs now, symptoms resolved, outcomes against the plan (9/8)
  - "Just saying stable isn't going to cut it" -> doctor reads it in clinical speak on a computer, patient gets a smaller version (9/8)
- Restructure the top level to progress-to-goal -> Kelly: the doctor doesn't need my step count, he needs am I following diet and exercise and did I lose the weight (9/8) - **Next**
  - The six category cards become the click-through detail, not the top level (9/8)
  - Symptom check at the top -> "has my hip pain resolved", ties to the how-am-I-feeling screens Kelly sent (9/8)
- v1 evaluation is pass-through, not a C4P scoring engine -> Greg: steal Apple, seven-day averages, "I don't care whether you calculate in our system" (9/8)
  - Start from meds, the daily log data already exists (9/8)
  - Narrowed 9/11: pass-through means our own 30-day averages against the goal, not Apple's evaluation -> Jay: a condition can mean more sleep or less (9/11)
- Fix the adherence numbers -> 80% overall has to reconcile with 95% daily dose before the demo (9/8) - **Next**
- "Recommend" becomes "consider" -> Orion is not the doctor (9/8) - **Next**
- Preference tag, not a preference editor -> Jay: preferences live in Orion memory, "we don't have to change anything here" (9/8)
- Catch-all provider field for what the six categories miss -> pain management, procedures, PT; patient marks aligned or not aligned (9/8)
  - PT combines with workout later, workout first (9/8)
- Labs and check-in cadence belong in the plan -> standing order for labs before the next visit, meeting frequency (9/8)
- Six categories are ratified -> medication, sleep, activity, nutrition, screenings, vaccines, and Jay's build list matches (9/8)
- Settled 9/11: Orion generates for every premium patient automatically, the provider generate button covers base patients, and the patient sees the plan either way (9/8, 9/11)
- Workout and recipe programs pulled in and customised to the record -> Greg's V Shred pitch (9/8) - **Pause**

### From the 9/11 team meeting

- Orion always generates the plan -> two triggers only: the provider clicks generate for a base patient, or the patient is premium and it generates automatically like vitality (9/11)
  - The provider sees the same plan either way and does not need to know the patient's tier (9/11)
  - A premium patient with no provider can still show theirs to a doctor afterwards (9/11)
- v1 has no patient editing at all -> not even premium; the patient sees the plan and their progress, the provider is the only editor (9/11) - **Next**
  - Pushback on a goal goes nowhere in v1 -> Orion can say build up to it, the number does not move (9/11)
  - Park the list of what a patient will eventually be able to change -> a note on a goal is the likely first one (9/11)
- Unreviewed plans carry a visible AI disclaimer -> drafted by Orion, not reviewed by your provider, review it before you follow it (9/11) - **Next**
- "Reviewed with patient" control on the provider side -> confirmed in the room at the visit, and it answers who generated the plan and whether it is signed off (9/11) - **Next**
- Design the provider-side plan on desktop -> Jay: we have to have it for the provider demos, generate plus edit, and where it lives in the provider UI is mine to decide (9/11) - **Next**
- Evaluation is the 30-day average against the goal -> Jay already shows 30-day averages, daily max across sources, on the provider side; put the goal beside the average (9/11) - **Next**
  - No good / bad / ugly status in v1 -> every status has to be defined and then explained to a provider (9/11)
  - Goals are Orion text today with no front end -> the target and the progress UI per metric are mine to draw (9/11)
- One schedule component for every goal type -> Jay wants the medication schedule UI reused, with defaults per category and some of it disabled (9/11) - **Next**
  - Not everything is a daily schedule -> workout and screenings run on their own cadence, sleep and diet are daily (9/11)
- Goals sync into the vitality categories, not just the plan -> a provider's eight-hour sleep goal shows under lifestyle and feeds the vitality evaluation (9/11)
  - Vitality shows the whole plan snapshot, Inside Health shows only its own care and lifestyle goals (9/11)
  - A goal repeating across categories is fine -> 10,000 steps can sit under metabolic health and lifestyle both (9/11)
  - Start with the six goals mapped across the three categories -> chronic conditions stay data and trends, not active goals (9/11)


## Prototype — Claude design

- Build the mobile patient app in the Claude design prototype, from the Figma screens (8/11)
  - ⇢ **parallel** — Build the json file to mock the live sync between provider app and patient app (8/11)
- Build the caregiver screens as a clickable prototype -> a lot of new entry points, need to check every button (8/25) - **Next**

## B2B — Provider Dashboard

- Full data sort & filter columns -> new tab in the logic / code Excel: every category, every table, every column, and for each column sort / filter / both + how (8/7) - **Pause, not the priority for now**
  - Map each element to a category from Kelly's Excel where it fits; flag the ones that don't (8/7)
  - Small UI snippets per column -> how sort shows (arrow), how filter is picked (chip, dropdown, text search) (8/7)
  - Link the snippets to the rows so Jay and Kelly can review in one place (8/7)
- Show the provider what the patient is and isn't sharing -> Kelly put it on me for phase two or three (9/4) - **Next**
  - Two problems, not one: a document center in the provider UI, and the sharing state itself (9/4)
- Providers want the actual source document, not the extracted care plan -> health system documents and patient uploads both (9/4) - **Next**
  - Orion answers already show document sources and View Document, citations aren't built out (9/4)
- Patient updates color coding -> drop the per-category colours since the feed mixes categories (9/4)
  - Kelly's worry: red was the only priority signal for the provider, watch the pilot feedback (9/4)
- No detail view anywhere in the provider UI except reports -> decide where a detail view lands (9/4)
  - Documentation reuses the document reviewer, single-data detail isn't finished on mobile either (9/4)
- Category column on the provider labs table -> Jay is adding it, it references the sub tab (9/4)
  - Provider feedback on the groupings comes back to the patient side so the two stay in sync (9/4)
- Suggested question pills: Kelly wants one click, I want the review step -> going to Portu testing instead of a redesign (9/4) - **Blocked**
  - [x] Jay widened the Orion chat box -> shipped 9/11, chips pinned to the input box, the view jumps to the top of the answer, sources on the patient summary (9/4)
- Diagnostic reports land in Full Data for now -> Jay's interim call before the release (9/4)
- Design how reports show in the provider UI -> Jay put them in Full Data to get live and calls it unusable; a report carries several observations plus documents, and the back step is wrong (9/11) - **Next**
- No secondary action anywhere on the provider dashboard -> that is my next pass, start with vitality and reports (9/11) - **Next**
- Decide what a provider actually needs from the vitality widget -> Jay filled it with subcategory summaries and data gaps so Dr. Porto has something to read (9/11)
- Full data groupings can be pushed to the dashboard -> Jay's plus button becomes my select-and-pin design, three columns max per item type (9/11)
- Medication source selection in the provider UI -> Jay will do it after meds and goals, Kelly needs it for the demo (9/11)

## Provider — Patient

- Jay may build the minimal patient–provider messaging himself -> stay aligned, don't block on it (8/7)
- Prescription refills -> Kelly added it to the list, it's a requirement for replacing a portal (9/1)
- Base patient access lasts as long as the provider contract, not 90 days -> check the paywall and expiry states and copy (9/4)
- Add picture / attach file in the chat box -> Greg's ChatGPT gap, supplement label photo, has to work on mobile for patients (9/8) - **Next**
  - I have an old add-button design, review and upgrade it with Jay (9/8)
- Summarize the notes a patient leaves along the timeline into the provider-facing patient update -> Kelly: patients forget what they meant to raise, keep visit essentials as the chief complaint (9/11) - **Next**
  - Check the visit essentials labels -> notes for my doctor and my notes have to read as two different things (9/11)
  - My notes is one component across the health hub; today Jay only stores notes on conditions, allergies and meds, and Orion reads them (9/11)


## Meds — add, schedule, log, tracking

- Make the FHIR code and the user-end input mapping.
- Celebration animation -> try the full screen design

## User Profile

- Emphasize the health ID / C4P account that user can share with other people.... even maybe combined with the health hub

---

## Done

_(nothing yet — move lines here with the date)_
