# Quiz App
The Quiz App is a platform designed to test your knowledge on specific topics or subjects of your choice.

## Features and Versions

For a detailed view of the features planned for each version of the Quiz Application, please refer to the Trello board at the following link: [Quiz App Project Trello Board](https://trello.com/b/TNlvvBdM/quiz-app-project).

This board provides a comprehensive overview of the features, milestones, and updates planned for each version of the application.


<--
**Zero-Based Versioning (0.x.x):**
- **Use Case:** For early development. Not yet stable or production-ready.
- **Example:** Version `0.1.0` to `0.2.0` for initial feedback and feature testing.

**Build/Revision Numbering (MAJOR.MINOR.BUILD or MAJOR.MINOR.BUILD.REVISION):**
- **Use Case:** For tracking individual builds and releases.
- **Example:** Version `1.0.0` to `1.1.0` with build number `1.1.0.100` for detailed build tracking.

### Features per Version

**Version 0.x.x (Early Development)**
- **Core Features:** Basic quiz creation, reading, and editing.
- **User Capabilities:** Create and share quizzes, basic question formats.
- **Limitations:** Initial performance and security features. For internal testing.

**Version 1.x.x (Initial Release)**
- **Enhanced Features:** Full quiz management, multiple question types, initial scoring system.
- **User Capabilities:** Public/private quizzes, sharing, basic analytics.
- **Improvements:** Improved performance and user interface.

**Version 1.1.x (Feature Expansion)**
- **Advanced Features:** Leaderboards, detailed explanations, post-quiz analytics.
- **User Capabilities:** Enhanced dashboard, integrated flashcards.
- **Improvements:** Performance optimization, additional analytics.

**Version 1.2.x (Stabilization and Optimization)**
- **Enhanced Features:** Online and offline modes, expanded timers, advanced scoring.
- **User Capabilities:** Robust analytics, improved offline functionality.
- **Improvements:** Bug fixes, security patches, infrastructure updates.

**Version 2.x.x (Major Update)**
- **New Features:** External tool integrations, advanced collaborative features.
- **User Capabilities:** Enhanced sharing, team-based quizzes, new learning tools.
- **Improvements:** Major performance upgrades, scalability enhancements, additional integrations.
-->




# Quiz Application Proposal

## Overview

The quiz app allows learners to test their knowledge through quizzes, while teachers can use the platform to assess students and provide solutions efficiently.

## Key Features

### Learner Capabilities
- **Create, Read, Edit, Delete Quizzes:** Manage quizzes with full control.
- **Share Quizzes:** Share quizzes with others, either publicly or privately.
- **Multiple Ownership:** Quizzes can be owned by multiple learners.
- **Teacher-Generated Quizzes:** Teachers can create quizzes to test students' knowledge.
- **Public Quizzes:** Quizzes can be created for public access.
- **Leaderboards:** Track and compare quiz performance.

### Quiz Structure
- **Questions:** Include text or images.
- **Answer Formats:** Multiple choice or essay.
- **Timers:** Set timers for each question and the entire quiz.
- **Scoring:** Each question can have different scores (default score: 1).
- **Explanations:** Provide explanations and resources for each option or essay.

### Post-Quiz Analytics
- **Time Tracking:** View time spent on each question.
- **Detailed Feedback:** Get explanations and resources for any mistakes.

### Online and Offline Modes
- **Offline Mode:** Self-test knowledge without internet.
- **Online Mode:** Share quizzes with teams, download from the server, or use by teachers.

### Dashboard
- **Performance Analysis:** Access all quizzes, view shared quizzes, start new ones, and manage friends and students.
- **Metrics:** Track quiz results, highest scores, and other performance metrics.

### Flashcards
- **Integration:** Possible addition of flashcards for enhanced learning support.

## Similar Projects
- [Quizizz](https://quizizz.com/)
- [Kahoot](https://kahoot.com/)
- [React Quiz App Example](https://github.com/VINAYAK9669/React-QuizApp)
- [GeeksforGeeks React Quiz Tutorial](https://www.geeksforgeeks.org/create-a-quiz-app-using-reactjs/)
- [Quiz Maker](https://www.quiz-maker.com/)
- [YouTube Video 1](https://www.youtube.com/watch?v=VMZ7lcSdVnY)
- [YouTube Video 2](https://www.youtube.com/watch?v=U1pn1cK_XqM)

## Methodology

### Agile (Kanban)
- **Kanban Board Setup:**
  - **Columns:** Backlog, To Do, In Progress, Review, Done.
  - **Tasks:** Add tasks as cards and move them through columns.
  - **WIP Limits:** Set limits to avoid bottlenecks.
  - **Review:** Regularly monitor progress and adjust priorities.

### DevOps
- **Continuous Integration (CI):** Automate code integration and testing.
- **Continuous Delivery (CD):** Automate deployment to staging or production.
- **Infrastructure as Code (IaC):** Use tools like Terraform or AWS CloudFormation.
- **Monitoring and Logging:** Tools like Prometheus, Grafana, and ELK Stack.
- **Automated Testing:** Tools like JUnit, PyTest, and Selenium.

### Tools for DevOps
- **Jenkins:** For automating CI/CD pipelines.
- **GitLab CI/CD:** Integrated CI/CD features.
- **CircleCI:** Cloud-based CI/CD tool.
- **Docker:** For containerization.
- **Kubernetes:** For orchestrating containerized applications.

## Software Versioning

### Versioning Types
- **Zero-Based Versioning (0.x.x):** Used during early development (e.g., 0.3.5).
- **Build/Revision Numbering:** Used for tracking builds (e.g., 1.2.456).

### Tools for Versioning
- **Git Version Tags:** Tag releases in Git.
- **Semantic Release:** Automate versioning and publishing.
- **Versioneer:** Manage version numbers in Python projects.

## Project Requirements

### Functional Requirements
- **Quiz Management:** Create, read, edit, delete quizzes and questions.
- **Answer Options:** Write or select answers/options.
- **Social Features:** Add friends, share quizzes, invite, and play with others.
- **Registration:** Register, log in, log out, and reset passwords with OTP.
- **Search:** Find public quizzes and request quizzes from friends.
- **Audio Support:** Enable audio for questions/options/resources.

### Non-Functional Requirements
- **Performance:** Handle thousands of users with zero downtime.
- **Availability:** Online and offline with 24/7 availability.
- **Security:** Encrypt and securely store user data.
- **Robustness:** Efficiently handle system failures.

## Software Design

The design ensures scalability, maintainability, and smooth integration with future updates.

## Software Development

### Frontend
- **Technologies:** ReactJS for SPAs, React Native for mobile apps.

### Backend
- **API:** FastAPI (integrated with Python for future ML integration).
- **Databases:** SQL for learner management, NoSQL for quizzes.

### Infrastructure
- **Cloud:** AWS or other cloud services.
- **OS:** Linux-based environment.
- **Version Control:** Git/GitHub.

## Software Testing

### Testing Types and Tools
- **Unit Tests:** PyTest (Python), Jest (JavaScript/React).
- **System Tests:** Selenium.
- **Integration Tests:** Postman, Cypress.
- **Functional Tests:** TestCafe, Cucumber.
- **End-to-End (E2E) Tests:** Cypress, Selenium.
- **Acceptance Testing:** Cucumber.
- **Performance Testing:** JMeter, Gatling, Apache Benchmark (ab), k6, Locust.
- **Smoke Testing:** Selenium, TestCafe.

## Software Maintenance

### Key Areas and Tools
1. **Bug Tracking and Issue Management:**
   - Jira, GitHub Issues, Bugzilla.
2. **Version Control and CI/CD:**
   - Git, GitHub/GitLab, Jenkins, CircleCI.
3. **Monitoring and Logging:**
   - Prometheus, Grafana, ELK Stack.
4. **Code Refactoring and Optimization:**
   - SonarQube, PyLint, ESLint.
5. **Security Patching and Vulnerability Management:**
   - Dependabot, Snyk, OWASP ZAP.
6. **Backup and Disaster Recovery:**
   - AWS Backup, Bacula, Restic.
7. **Software Updates and Release Management:**
   - GitLab CI, Helm, Docker.
8. **Documentation Management:**
   - Docusaurus, Confluence, MkDocs.

### Best Practices
- **Regular Monitoring:** Continuously monitor performance and logs.
- **Apply Security Patches:** Regular updates and security patches.
- **Refactor Code Periodically:** Clean and optimize codebase.
- **Backup and Disaster Recovery:** Regular backups and recovery planning.
- **Update Documentation:** Maintain detailed technical documentation.

