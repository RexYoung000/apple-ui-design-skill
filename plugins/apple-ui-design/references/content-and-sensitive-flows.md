# Content and Sensitive Flows

## Load When

Load this reference when content changes consequential meaning, consent, protected access, authentication, account data, destructive action, commerce, recovery, or a regulated professional claim. Do not load it for ordinary visual polish with no change to meaning, control, consequence, or recovery.

This is the single runtime source for sensitive-flow content and control. The direction skill defines the intended flow, the adaptation skill translates confirmed behavior, and the review skill assesses supplied evidence. None owns legal, medical, financial, security, privacy-policy, pricing, refund, tax, or App Store compliance decisions.

## Contents

- Decision and source boundary
- Sensitive-flow contract
- Product content and recovery
- Permission and privacy
- Identity and account data
- Subscriptions and purchases
- Regulated professional domains
- Manipulation checks
- Evidence and acceptance

## Decision and Source Boundary

Separate these inputs before designing:

- **Confirmed product fact**: the actual feature, data use, price, entitlement, retention behavior, account rule, or support path supplied by the responsible project owner.
- **Current official source**: the exact Apple page and access date for platform guidance, App Store policy, StoreKit behavior, or system capability.
- **Professional decision**: a legal, privacy, security, clinical, financial, tax, refund, or regulatory conclusion owned by an authorized specialist.
- **Design inference**: a proposed hierarchy, wording, interaction, or recovery model that helps the user understand and act.
- **Unverified placeholder**: missing content or policy that must remain visibly unresolved and must not ship as invented fact.

Use `current-sources.md` for changeable Apple claims. Do not quote a remembered policy, invent a product term, or turn a design recommendation into compliance approval. If an unresolved fact changes consent, payment, data loss, eligibility, or professional meaning, stop only the affected artifact and route the decision to its owner.

## Sensitive-Flow Contract

For every material flow, define:

1. **When it appears** — the user action or state that justifies the flow now.
2. **User outcome** — what the user is trying to understand, permit, buy, recover, export, delete, or decide.
3. **Verified facts and owner** — the product, policy, data, price, entitlement, or professional facts the interface may state, plus who confirms them.
4. **Content hierarchy** — the primary fact, consequence, supporting detail, primary action, alternative, and help path.
5. **User control** — accept, decline, defer, dismiss, change, revoke, restore, cancel, or return behavior as applicable.
6. **System boundary** — what belongs to the app, an Apple system prompt, Settings, StoreKit, authentication service, support process, or another external surface.
7. **States and consequences** — not determined, in progress, allowed, limited, denied, pending, succeeded, failed, expired, cancelled, restored, or partially completed as relevant.
8. **Failure and recovery** — what remains unchanged, what can be retried, how the user returns, and when support or escalation is real.
9. **Accessibility and localization** — semantic action and state, reading order, non-color meaning, content expansion, locale formats, and translated acceptance.
10. **Evidence** — source review, design artifact, operable prototype, native or sandbox run, data-operation result, professional sign-off, and remaining gaps.

Keep the contract proportional to the risk. A low-consequence empty state does not need the same review depth as account deletion or a recurring purchase.

## Product Content and Recovery

Use this method for labels, button copy, onboarding, empty states, errors, confirmations, progress, completion, and recovery where wording changes user understanding or action.

- Lead with the fact or user outcome, not internal system terminology.
- Make a consequential action describe what it does. Avoid ambiguous `Yes`, `Continue`, or `Done` when the result matters.
- For an empty state, distinguish no data, filtered data, unavailable data, missing access, and first use; offer only an action the product can actually perform.
- For an error, state what failed, the user-visible impact, what was preserved, and the next valid action. Do not blame the user or show a raw error code as the only explanation.
- Keep loading, pending, partial, offline, cancelled, success, and failure language consistent with the real state. Never display success before the operation is confirmed.
- Use project voice without hiding consequence. Calm or playful tone may not make a destructive, private, or paid action ambiguous.

Do not infer backend state, support availability, processing time, saved progress, or recoverability from a screen design. Verify these as product or runtime facts.

## Permission and Privacy

Use this method when the product requests protected data or a system capability, explains data use, changes consent, or displays sensitive information.

- Ask in the context of a user-initiated feature and explain the specific value and resource before the system handoff when that explanation is useful.
- Keep the app explanation visually distinct from the real system prompt. Do not simulate a permission alert and claim native behavior.
- Request only access relevant to the task and prefer a narrower picker or user-selected path when it satisfies the product outcome.
- Respect denial, limited access, restriction, or deferred choice. Define what remains usable, a truthful alternative when one exists, and a Settings or retry path only when it can help.
- Do not repeatedly pressure after refusal, shame the user, make unrelated paid functionality conditional on unnecessary access, or falsely claim the product cannot work.
- State data collection, use, sharing, retention, and withdrawal behavior only from confirmed product and policy facts. Minimize disclosure in the interface without omitting a material consequence.
- Protect sensitive content before authorization and avoid exposing it in previews, notifications, logs, screenshots, or shared surfaces unless the project explicitly defines and verifies that behavior.

If no alternative can complete the requested feature without permission, explain that dependency and leave the rest of the product usable where possible. The fallback is clarity and recovery, not a fake equivalent.

## Identity and Account Data

Use this method for sign-in, account creation, reauthentication, credential or session recovery, data export, consent withdrawal, account deletion, and other sensitive account actions.

- Require an account only when confirmed product capability or current policy supports that dependency; do not invent mandatory registration for convenience.
- Explain why reauthentication is needed without exposing security-sensitive detail. The security owner defines factors, lockout, session, and recovery policy.
- Preserve entered work and return context across sign-in or verification whenever the actual product supports it.
- Make export scope, format, preparation state, delivery path, expiration, failure, and retry behavior explicit from project facts.
- Make deletion easy to find and state its scope, consequences, processing time, subscription interaction, retained data, cancellation window, confirmation, and completion only when those facts are verified.
- Use proportionate confirmation for destructive actions. Confirmation may protect intent; it may not become unnecessary obstruction.
- Do not imply that deleting an app, signing out, revoking a token, cancelling a subscription, deleting content, and deleting an account are the same operation.

Account and data-operation completion requires real service evidence. A prototype can validate comprehension and flow continuity only.

## Subscriptions and Purchases

Use this method for paywalls, trials, subscription selection, purchase confirmation, entitlement state, restoration, cancellation or management paths, refunds, and failed or pending transactions.

- Verify the product, included value, duration, amount billed, renewal behavior, trial or offer consequence, eligibility, and localized price from the real commerce source.
- Make the amount actually billed the primary price. Keep derived monthly equivalents or savings subordinate and mathematically accurate.
- For a trial, state its duration and the amount and cadence that follow it. Do not use fake scarcity, countdowns, preselected consent, or ambiguous free language.
- Provide honest dismissal or defer behavior when the product permits it. Do not hide a close path, visually disguise the nonpurchase choice, or shame people who decline.
- Define purchasing, pending, succeeded, failed, cancelled, restored, expired, billing-retry, and entitlement-refresh states as applicable. Do not unlock or report success before verified entitlement.
- Provide the real sign-in, restore, manage, or cancel path supported by the product and current Apple policy. Do not invent in-app cancellation, refund eligibility, tax treatment, or storefront availability.
- Keep account deletion and active billing consequences connected so the user does not mistake one for the other.

Static paywalls and browser prototypes can support hierarchy and content review. Native StoreKit or sandbox execution is required for purchase, restoration, entitlement, pending-state, and management behavior claims.

## Regulated Professional Domains

Use this method when the interface presents or acts on health, medical, financial, legal, safety, gambling, aviation, crypto, or another regulated or high-consequence claim.

- Identify the responsible professional, legal entity, approved source, jurisdiction, review date, and intended audience where the product requires them.
- Separate recorded fact, calculation, recommendation, prediction, and professional advice in both content and hierarchy.
- Do not diagnose, prescribe, guarantee, approve eligibility, promise returns, interpret law, or invent an emergency path from general design knowledge.
- Do not add a generic disclaimer as a substitute for expert review or for fixing a misleading claim.
- Show uncertainty, limitations, source age, escalation, and human review only when the responsible owner has defined them.
- Fail safely when a required professional fact or approval is missing: label the affected content unverified, block only that claim or action, and route it to the named owner.

The design skill can improve comprehension, control, hierarchy, accessibility, and recovery. It cannot certify clinical safety, financial suitability, legal compliance, or regulatory approval.

## Manipulation Checks

Treat these as blocking when they materially distort consent, purchase, privacy, or destructive consequences:

- false urgency, scarcity, savings, success, or authority;
- preselected consent or an action whose label hides its consequence;
- repeated pressure after a clear decline;
- shame, fear, or loss framing unrelated to a verified consequence;
- hidden, moving, delayed, or visually disguised decline, dismiss, restore, manage, export, or delete paths;
- unequal information, such as emphasizing a derived low price while obscuring the billed amount;
- bundling unnecessary access or personal data with unrelated functionality;
- claiming professional or legal certainty without an authorized source.

Visual emphasis can express a recommended action or product priority. It may not remove an informed, operable choice or misrepresent the outcome.

## Evidence and Acceptance

Match evidence to the claim:

- content inventory and source review establish wording inputs and missing facts;
- rendered screens establish hierarchy, visibility, and content fit;
- an operable prototype establishes the exercised app-level path and recovery model;
- native permission and Settings runs establish the exercised system handoff and access states;
- authentication and data-service runs establish the exercised account, export, or deletion behavior;
- StoreKit sandbox or approved test-environment runs establish the exercised purchase and entitlement behavior;
- professional sign-off establishes only the reviewed claim, jurisdiction, scope, and version;
- user acceptance establishes final tone, trust, and commercial presentation.

Record the source date, environment, account or entitlement state, locale and storefront when relevant, path exercised, observed result, and unverified scenarios. Do not report a copy review as policy approval, a mocked prompt as permission evidence, a static paywall as purchase validation, or an expert-looking disclaimer as professional review.
