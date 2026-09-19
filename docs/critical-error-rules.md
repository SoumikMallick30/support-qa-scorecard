# Critical Error Rules

Critical errors are serious failures that may override the normal numerical QA score.

This framework provides general examples. Each organization should customize critical-error definitions according to its own policies, legal requirements, security standards, and business processes.

---

## 1. Privacy and Data Security

A critical error may occur when an agent:

- Shares sensitive customer information with an unauthorized person
- Exposes account or personal information incorrectly
- Requests or stores prohibited sensitive information
- Violates required privacy or data-security procedures

### Example

An agent provides account information before completing mandatory identity verification.

**Suggested classification:** Critical Error

---

## 2. Mandatory Verification Failure

A critical error may occur when required customer or account verification is skipped.

Examples:

- Accessing protected account information without required verification
- Making account changes before completing mandatory authentication
- Accepting insufficient verification when policy requires additional checks

### Important

Minor procedural mistakes that do not compromise required verification should not automatically be classified as critical.

---

## 3. Unauthorized Account Actions

Examples include:

- Making a refund without required authorization
- Changing account information without proper verification
- Cancelling or modifying a service without authorization
- Performing actions outside the agent's permitted access or role

**Suggested classification:** Critical Error when the action creates meaningful customer, security, compliance, or financial risk.

---

## 4. Materially Incorrect Information

Incorrect information may qualify as a critical error when it could cause significant harm to the customer or organization.

Examples:

- Providing materially incorrect financial information
- Giving incorrect instructions that could cause account loss or service disruption
- Making unsupported guarantees or commitments
- Providing materially incorrect policy information

Minor inaccuracies should normally be handled through standard point deductions rather than automatic critical-error classification.

---

## 5. Compliance or Regulatory Failure

A critical error may occur when an agent violates a mandatory legal, regulatory, or organizational compliance requirement.

The exact definition depends on the industry and organization.

Examples may include:

- Missing mandatory disclosures
- Violating required consent procedures
- Mishandling protected customer information
- Ignoring mandatory compliance steps

---

## 6. Intentional Interaction Avoidance

Possible examples include:

- Intentionally disconnecting an interaction to avoid handling it
- Unnecessarily transferring a customer to avoid ownership
- Manipulating interaction status or workflow
- Intentionally providing no meaningful assistance

These cases should be supported by clear evidence before being classified as critical.

---

# Critical vs Non-Critical Errors

Not every QA failure should be classified as critical.

| Example | Typical Treatment |
| --- | --- |
| Minor grammar mistake | Point deduction |
| Slightly weak empathy | Point deduction |
| Incomplete closing | Point deduction |
| Minor documentation issue | Point deduction |
| Serious privacy violation | Potential critical error |
| Mandatory verification skipped | Potential critical error |
| Unauthorized account action | Potential critical error |
| Serious harmful misinformation | Potential critical error |

---

# Recommended Critical-Error Workflow

When a potential critical error is identified:

1. Document the exact behavior or action.
2. Identify the policy or requirement involved.
3. Record supporting evidence from the interaction.
4. Confirm that the event meets the organization's critical-error definition.
5. Escalate for review when required.
6. Record the final classification and rationale.

---

# Effect on QA Score

Organizations can choose how critical errors affect the final score.

Common approaches include:

### Automatic Failure

The interaction receives a failing QA result regardless of the numerical score.

### Zero Final Score

The numerical score is replaced with zero.

### Category Failure

Only the affected category receives zero points.

### Separate Critical-Error Flag

The numerical score remains unchanged, but the interaction is separately marked as a critical failure.

This project does not prescribe one universal approach because organizations have different policies and risk requirements.

---

# Critical Error Review Template

**Critical Error Identified:** Yes / No

**Category:**

**Interaction Evidence:**

**Policy / Requirement Affected:**

**Customer or Business Impact:**

**Evaluator Rationale:**

**Reviewer Decision:**

**Corrective / Coaching Action:**

---

# Calibration Guidance

Critical-error decisions should be included in QA calibration sessions.

Teams should periodically review:

- Whether evaluators classify similar failures consistently
- Whether critical-error definitions are sufficiently clear
- Whether policies have changed
- Whether recurring critical errors indicate a training or process gap

---

## Disclaimer

These rules are a general open-source QA framework and are not legal, regulatory, security, or compliance advice.

Organizations should adapt the framework to their own policies and applicable requirements.
