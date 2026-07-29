# LedgerDesk Status and Action System

Status: existing macOS product

- Primary task: reconcile incoming payments with issued invoices.
- A wrong match has high financial cost.
- Product character: calm, precise, professional, and not bank-like.
- Shipped locales: English and German.
- Required inputs: keyboard, pointer, and VoiceOver.
- Existing project values:
  - background `#F4F1EB`;
  - primary text `#242321`;
  - accent `#2F675D`;
  - warning `#B46A24`;
  - critical `#A53B36`;
  - corner radii currently vary between 6, 8, and 12 points without documented meaning.
- Current problems:
  - selected rows and resolved rows both use pale green;
  - warning badges and destructive actions both use orange;
  - primary, secondary, and disabled actions vary by screen;
  - keyboard focus is not represented in the component specification.
- Required component coverage: reconciliation row, status badge, primary action, secondary action, destructive action, and focus treatment.
- Representative German content: “Zahlung konnte keiner Rechnung zugeordnet werden” and “Als geklärt markieren”.
- Do not redesign product navigation in this task.
