const test = require("node:test");
const assert = require("node:assert/strict");
const { evaluateScores, getRating, reportToCsv } = require("../web/app.js");

const perfectScores = {
  communication: 20,
  understanding: 20,
  resolution: 30,
  compliance: 15,
  experience: 15
};

test("rating boundaries match the documented rubric", () => {
  assert.equal(getRating(90), "Excellent");
  assert.equal(getRating(80), "Meets Expectations");
  assert.equal(getRating(70), "Needs Improvement");
  assert.equal(getRating(69), "Unsatisfactory");
});

test("evaluation calculates totals and critical failures", () => {
  const result = evaluateScores(perfectScores, true);
  assert.equal(result.totalScore, 100);
  assert.equal(result.rating, "Excellent");
  assert.equal(result.resultFlag, "CRITICAL FAILURE");
});

test("evaluation rejects out-of-range category scores", () => {
  assert.throws(
    () => evaluateScores({ ...perfectScores, compliance: 16 }, false),
    RangeError
  );
});

test("CSV export safely quotes commas, quotes, and newlines", () => {
  const report = {
    ...evaluateScores(perfectScores, false),
    agentName: "Doe, Jane",
    interactionId: "CASE-1",
    qaAnalyst: "Alex",
    qaFeedback: 'Clear, "helpful" response',
    coachingNotes: "Follow up\nnext week",
    generatedAt: "2026-09-21T12:00:00.000Z"
  };
  const csv = reportToCsv(report);
  assert.match(csv, /"Doe, Jane"/);
  assert.match(csv, /"Clear, ""helpful"" response"/);
  assert.match(csv, /"Follow up\nnext week"/);
});
