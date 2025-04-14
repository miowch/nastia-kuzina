# Exploratory Testing Session of the Monefy app

## Exploratory testing charters to document your testing

### Feature Tour

Priority: High
Reasoning: Explore core features individually and ensure they behave correctly.

- Onboarding \
   Finding on the Welcome screen: Say hi to your new finance tracker -> Say Hi...
- Add expense \
   Findings:
  1. Bug: When a note contains emoji or special char (includ. Cyrillic or letters with umlauts), an empty suggestion is displayed. Selecting the suggestion clears the note.
  1. No Clear icon for the Note field
  1. It would be nice to close the keyboard by clicking outside it on the new expense screen
- Add income
- Add account
- Transfer money between accounts
- Edit entry
- Delete entry / undo deletion
- View summary by category
- View entries by time range \
  Finding: \
  It is possible to unselect default sorting tab Day. Expected: selected time frame is marked with color.
- Change currency \
  Findings:
  1. There is no autoconversion\
  1. All previous records get new currency and old values
- Search transactions: by category name, by value, by note, by account \
  Findings:
  1. Search by 4 -> only entries with 4.00 value are displayed. Expected result: entries with 4.99 value or with 4 in notes are displayed
  1. Message about finding no records says that it is possible to search only for category, account or note. It is possible to search also for value.
  1. Trailing spaces get removed from search. Nice
- Change language

### Landmark Tour

Priority: High
Reasoning: Focus on critical areas where users spend the most time.

- Add/Edit transaction screen
- Category view : clicking on sector opens balance with extended category, clicking on sector Others opens balance with all categories included to this aggregation extended
- Settings \
  Findings:
  1. No way to get 7 days free subscription after leaving welcome screens
  1. Budget mode: example (0)/previous value is not removed by default, new chars are added to the end
  1. Data restoration is not user-friendly because the message looks unclickable

### Data Tour

Priority: High
Reasoning: Use a variety of input data and edge cases.

- Adding an expense with past/future date
- Adding math expression as a value of expense/income \
  Finding: The clear icon removes the last part of the expression instead of the whole value
- Very large amounts (e.g. 999999.99)
- Invalid values (e.g. letters instead of numbers)
- Emojis or special characters in notes
- Missing fields / blank values
- Long text inputs

### Interrupt Tour

Priority: High
Reasoning: Introduce real-world mobile disruptions.

- Lock/unlock phone mid-task
- Switch apps and return
- Lose internet during use
- Testing offline mode (if supported)

### Other example charters that could have explored

#### User Persona Tour

Priority: Medium
Reasoning: Act like different types of users.

#### Language/Currency/Locale Tour

Priority: Medium
Reasoning: Play with regional settings.

#### Supermodel Tour

Priority: Low
Reasoning: Put the UI/UX under a spotlight.

## What kind of risks do you need to mitigate for this type of application?

| Risk Area            | Priority  | Why                                |
| -------------------- | --------- | ---------------------------------- |
| Data loss/corruption | 🔥 High   | Breaks trust, hard to recover      |
| Currency handling    | 🔥 High   | Core function, high chance of bugs |
| Incorrect totals     | 🔥 High   | Undermines purpose of app          |
| Offline scenarios    | ⚠️ Medium | May go unnoticed until too late    |
| UI inconsistencies   | ⚠️ Medium | Frustrates users, kills retention  |
| Localization bugs    | ⚠️ Medium | Easy to miss, affects global use   |
