# State and transition map

```mermaid
flowchart TD
    A["Welcome"] -->|Get started| B["Why access is needed"]
    B -->|Choose photos| C["Mock system-permission handoff"]
    C -->|Don't allow| D["Permission denied"]
    D -->|Try again| C
    D -->|Not now| A
    C -->|Allow selected photos| E["Limited access confirmed"]
    E -->|Continue| F["Mock photo selection"]
    F -->|Cancel| B
    F -->|Select 1+ and import| G["Importing"]
    G -->|Cancel import| F
    G -->|Mock success| J["First collection complete"]
    G -->|Mock recoverable failure| H["Import failed"]
    H -->|Retry import| G
    H -->|Review selection| F
    J -->|Reset prototype| A
```

## State rules

| State | Primary action | Secondary/cancel action | Preserved data |
|---|---|---|---|
| Welcome | Get started | None | None |
| Explanation | Choose photos | Back | None |
| Permission handoff (mocked) | Allow selected photos | Don’t allow | Trigger focus |
| Denied | Try again | Not now | Denial meaning |
| Limited access | Continue | Back | Limited grant |
| Selection (mocked) | Import selected | Cancel | Selected mock photo IDs |
| Importing | Wait for result | Cancel import | Selected mock photo IDs |
| Recoverable failure | Retry import | Review selection | Selected mock photo IDs |
| Completion | Reset prototype | None | Imported mock photo IDs |

## Prototype controls

The “next import result” control is outside the app surface. It exists only to make the recoverable-failure path deterministic and operable. Permission results remain inside a clearly labelled simulated system sheet so the user can operate denial and retry directly.
