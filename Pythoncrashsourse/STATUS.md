# Translation status

Một dòng cho mỗi unit (file). Cập nhật cột **Status** mỗi khi trạng thái thay đổi.

Trạng thái: `NOT_STARTED` → `EXTRACTED` → `TRANSLATING` → `TRANSLATED` → `QA` → `COMPLETED`
(`SKIP` = không dịch, chỉ để tham khảo.)

- `TRANSLATING`: `translated/<unit>.md` đang được viết dở. Cột Notes ghi trang PDF cuối cùng đã dịch,
  ví dụ `done to pdf-page 44` — phiên sau dịch tiếp từ đó, không dịch lại.
- `COMPLETED`: chỉ sau khi người dùng xác nhận chương đã ổn. Không bao giờ dịch lại unit `COMPLETED`.

| # | Unit | Title | PDF pages | Printed pages | Code blocks | Status | Notes |
|---|---|---|---|---|---|---|---|
| 0 | front-matter | Front Matter | 1–27 | roman | 69 | SKIP | reference only (cover, TOC) |
| 1 | acknowledgments | Acknowledgments | 28–29 | roman | 0 | QA |  |
| 2 | introduction | Introduction | 30–33 | roman | 1 | QA |  |
| 3 | part-1 | Part I: Basics | 34–35 | 1–2 | 0 | QA |  |
| 4 | chapter-01 | Chapter 1: Getting Started | 36–51 | 3–18 | 27 | QA |  |
| 5 | chapter-02 | Chapter 2: Variables and Simple Data Types | 52–69 | 19–36 | 52 | QA |  |
| 6 | chapter-03 | Chapter 3: Introducing Lists | 70–85 | 37–52 | 47 | QA |  |
| 7 | chapter-04 | Chapter 4: Working with Lists | 86–107 | 53–74 | 61 | QA |  |
| 8 | chapter-05 | Chapter 5: if Statements | 108–127 | 75–94 | 47 | QA |  |
| 9 | chapter-06 | Chapter 6: Dictionaries | 128–149 | 95–116 | 58 | QA |  |
| 10 | chapter-07 | Chapter 7: User Input and while Loops | 150–165 | 117–132 | 34 | QA |  |
| 11 | chapter-08 | Chapter 8: Functions | 166–193 | 133–160 | 68 | QA |  |
| 12 | chapter-09 | Chapter 9: Classes | 194–221 | 161–188 | 49 | QA |  |
| 13 | chapter-10 | Chapter 10: Files and Exceptions | 222–247 | 189–214 | 66 | QA |  |
| 14 | chapter-11 | Chapter 11: Testing Your Code | 248–263 | 215–230 | 20 | QA |  |
| 15 | part-2 | Part II: Projects | 264–265 | 231–232 | 0 | QA |  |
| 16 | project-1 | Project 1: Alien Invasion | 266–267 | 233–234 | 0 | QA |  |
| 17 | chapter-12 | Chapter 12: A Ship that Fires Bullets | 268–297 | 235–264 | 48 | EXTRACTED |  |
| 18 | chapter-13 | Chapter 13: Aliens! | 298–323 | 265–290 | 40 | EXTRACTED |  |
| 19 | chapter-14 | Chapter 14: Scoring | 324–351 | 291–318 | 55 | EXTRACTED |  |
| 20 | project-2 | Project 2: Data Visualization | 352–353 | 319–320 | 0 | QA |  |
| 21 | chapter-15 | Chapter 15: Generating Data | 354–381 | 321–348 | 40 | EXTRACTED |  |
| 22 | chapter-16 | Chapter 16: Downloading Data | 382–409 | 349–376 | 47 | EXTRACTED |  |
| 23 | chapter-17 | Chapter 17: Working with APIs | 410–427 | 377–394 | 21 | EXTRACTED |  |
| 24 | project-3 | Project 3: Web Applications | 428–429 | 395–396 | 0 | QA |  |
| 25 | chapter-18 | Chapter 18: Getting Started with Django | 430–459 | 397–426 | 44 | EXTRACTED |  |
| 26 | chapter-19 | Chapter 19: User Accounts | 460–487 | 427–454 | 39 | EXTRACTED |  |
| 27 | chapter-20 | Chapter 20: Styling and Deploying an App | 488–515 | 455–482 | 43 | EXTRACTED |  |
| 28 | afterword | Afterword | 516–517 | 483–484 | 0 | QA |  |
| 29 | appendix-a | Appendix A: Installing Python | 518–523 | 485–490 | 15 | EXTRACTED |  |
| 30 | appendix-b | Appendix B: Text Editors | 524–531 | 491–498 | 14 | EXTRACTED |  |
| 31 | appendix-c | Appendix C: Getting Help | 532–537 | 499–504 | 3 | EXTRACTED |  |
| 32 | appendix-d | Appendix D: Using Git for Version Control | 538–547 | 505–514 | 21 | EXTRACTED |  |
| 33 | index | Index | 548–562 | 515–529 | 1 | SKIP | index page numbers refer to the English edition |
