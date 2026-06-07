# AI_response_evaluator

This framework evaluates AI-generated answers using three focused tests that target the most common failure modes: fake sources, unsupported claims, and logical inconsistency.

---

## 1. Verifiable Evidence Test (VET)

Checks whether citations, URLs, studies, reports, or organizations mentioned in the answer actually exist and can be verified.

**Why it matters:**  
AI models often generate convincing but fake references. VET ensures all external sources are real and traceable.

**Output:** Flags hallucinated or unverifiable sources.

---

## 2. Claim Support Test (CST)

Checks whether factual statements (statistics, dates, rankings, causal claims, measurements) are supported by evidence.

**Why it matters:**  
Models frequently assert facts without justification. CST ensures claims are grounded rather than assumed.

**Output:** Flags unsupported or weakly supported claims.

---

## 3. Consistency Test (CT)

Checks whether the answer is logically consistent and free from contradictions.

**Why it matters:**  
Even accurate facts can become unreliable if the response contradicts itself or changes assumptions.

**Output:** Flags internal contradictions or conflicting statements.

---

## Why these three?

| Test | Focus |
|------|------|
| VET | Validity of sources |
| CST | Strength of factual claims |
| CT  | Logical consistency |

Together, they cover the three main hallucination risks in AI responses: **fake evidence, unsupported facts, and internal inconsistency**.
