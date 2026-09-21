(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  } else {
    root.QAScorecard = api;
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  const fields = [
    { id: "communication", label: "Communication & Professionalism", max: 20 },
    { id: "understanding", label: "Understanding the Customer's Issue", max: 20 },
    { id: "resolution", label: "Resolution & Accuracy", max: 30 },
    { id: "compliance", label: "Process Compliance", max: 15 },
    { id: "experience", label: "Customer Experience", max: 15 }
  ];

  function getRating(score) {
    if (score >= 90) return "Excellent";
    if (score >= 80) return "Meets Expectations";
    if (score >= 70) return "Needs Improvement";
    return "Unsatisfactory";
  }

  function evaluateScores(scores, criticalError) {
    let total = 0;
    const validatedScores = {};

    fields.forEach(function (field) {
      const value = Number(scores[field.id]);
      if (!Number.isFinite(value) || value < 0 || value > field.max) {
        throw new RangeError(field.label + " must be between 0 and " + field.max + ".");
      }
      validatedScores[field.id] = value;
      total += value;
    });

    return {
      scores: validatedScores,
      totalScore: total,
      rating: getRating(total),
      criticalError: Boolean(criticalError),
      resultFlag: criticalError ? "CRITICAL FAILURE" : "Standard numerical result"
    };
  }

  function csvEscape(value) {
    const text = String(value == null ? "" : value);
    return /[",\n]/.test(text) ? '"' + text.replace(/"/g, '""') + '"' : text;
  }

  function reportToCsv(report) {
    const rows = [
      ["Field", "Value"],
      ["Agent Name", report.agentName],
      ["Interaction ID", report.interactionId],
      ["QA Analyst", report.qaAnalyst]
    ];
    fields.forEach(function (field) {
      rows.push([field.label + " (max " + field.max + ")", report.scores[field.id]]);
    });
    rows.push(
      ["Total Score", report.totalScore],
      ["Rating", report.rating],
      ["Critical Error", report.criticalError ? "Yes" : "No"],
      ["Result Flag", report.resultFlag],
      ["QA Feedback", report.qaFeedback],
      ["Coaching Notes", report.coachingNotes],
      ["Generated At", report.generatedAt]
    );
    return rows.map(function (row) { return row.map(csvEscape).join(","); }).join("\n");
  }

  function initializeBrowser() {
    if (typeof document === "undefined") return;
    let currentReport = null;

    function value(id) {
      return document.getElementById(id).value.trim();
    }

    function download(content, type, filename) {
      const link = document.createElement("a");
      link.href = URL.createObjectURL(new Blob([content], { type: type }));
      link.download = filename;
      link.click();
      URL.revokeObjectURL(link.href);
    }

    document.getElementById("calculateBtn").addEventListener("click", function () {
      const error = document.getElementById("validationError");
      const scores = {};
      error.textContent = "";

      for (const field of fields) {
        const input = document.getElementById(field.id);
        if (input.value.trim() === "") {
          error.textContent = "Enter a score for " + field.label + ".";
          input.focus();
          return;
        }
        scores[field.id] = input.value;
      }

      try {
        currentReport = Object.assign(
          {
            agentName: value("agentName"),
            interactionId: value("interactionId"),
            qaAnalyst: value("qaAnalyst"),
            qaFeedback: value("qaFeedback"),
            coachingNotes: value("coachingNotes"),
            generatedAt: new Date().toISOString()
          },
          evaluateScores(scores, value("critical") === "yes")
        );
      } catch (validationError) {
        error.textContent = validationError.message;
        return;
      }

      document.getElementById("score").textContent = currentReport.totalScore + " / 100";
      document.getElementById("rating").textContent = "Rating: " + currentReport.rating;
      const status = document.getElementById("status");
      status.className = "status " + (currentReport.criticalError ? "error" : "success");
      status.textContent = "Critical Error: " + (currentReport.criticalError ? "YES" : "NO") +
        " | Result Flag: " + currentReport.resultFlag;
      document.getElementById("result").style.display = "block";
      document.getElementById("reportActions").hidden = false;
    });

    document.getElementById("downloadJsonBtn").addEventListener("click", function () {
      download(JSON.stringify(currentReport, null, 2), "application/json", "qa-evaluation.json");
    });
    document.getElementById("downloadCsvBtn").addEventListener("click", function () {
      download(reportToCsv(currentReport), "text/csv;charset=utf-8", "qa-evaluation.csv");
    });
    document.getElementById("printReportBtn").addEventListener("click", function () {
      window.print();
    });
  }

  if (typeof window !== "undefined") {
    window.addEventListener("DOMContentLoaded", initializeBrowser);
  }

  return { fields: fields, getRating: getRating, evaluateScores: evaluateScores, reportToCsv: reportToCsv };
});
