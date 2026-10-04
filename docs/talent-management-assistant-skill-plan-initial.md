# Implementation Plan: Talent Management Assistant Skill

## Introduction

This document outlines a detailed implementation plan for the **Talent Management Assistant Skill**, designed to automate and streamline the management of talent profiles across various verticals. This skill will be integrated into the `ke-skill-set` repository and will leverage Manus capabilities to enhance operational efficiency and data consistency, drawing directly from the "Entertainment Management Dashboard Specifications (V2)" [1].

## 1. Core Architecture and Data Models

### 1.1. Skill Definition (`SKILL.md`)

The skill will be defined by a `SKILL.md` file, outlining its purpose, core functionalities, input parameters, and expected outputs. This will serve as the primary interface for interacting with the skill.

### 1.2. Data Persistence Strategy

For initial implementation, data will be managed using file-based storage (e.g., JSON files within the skill's directory) to represent talent profiles. This approach allows for rapid prototyping and iteration. Future enhancements could involve integration with external database APIs for scalable enterprise solutions.

### 1.3. Talent Data Models

Each talent vertical will have a distinct data model, capturing specific metrics and attributes. These models will be represented as structured data (e.g., JSON objects) within the skill's storage.

#### 1.3.1. Music Artist Profile Model

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the artist. |
| `name` | String | Artist's stage name or group name. |
| `type` | Enum | `Solo` or `Duo/Group`. |
| `genre` | String | Primary music genre. |
| `name_registries` | Array | List of registered names (e.g., ASCAP, BMI). |
| `streaming_counters`| Object | Key-value pairs for streaming platforms (e.g., `spotify: 1.2M`, `apple_music: 800K`). |
| `follower_counts` | Object | Key-value pairs for social media platforms (e.g., `instagram: 500K`, `tiktok: 1M`). |
| `monthly_listeners` | Integer | Global monthly listener count. |
| `contact_info` | Object | Email, phone, manager contact. |
| `status` | Enum | `Active`, `On Hiatus`, `Archived`. |

#### 1.3.2. Model Profile Model

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the model. |
| `name` | String | Model's full name. |
| `gender` | Enum | `Male`, `Female`, `Other`. |
| `physical_stats` | Object | Height, weight, measurements, eye color, hair color. |
| `portfolio_specs` | Array | Links to portfolio, comp cards. |
| `lookbook_registries`| Array | List of associated lookbooks. |
| `brand_ambassador_contracts` | Array | List of active brand ambassador contracts. |
| `agency_representations` | Array | List of agencies representing the model. |
| `contact_info` | Object | Email, phone, agent contact. |
| `status` | Enum | `Active`, `Inactive`, `Archived`. |

#### 1.3.3. Child Model Profile Model (High Security Layer)

This model will inherit from the `Model Profile Model` and include additional security-focused fields.

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the child model. |
| `name` | String | Child model's full name. |
| `parent_guardian_name` | String | Full name of the parent or legal guardian. |
| `parent_contact_info` | Object | Parent's email, phone. |
| `parental_approval` | Boolean | **CRITICAL**: `true` if parental approval is verified for media/bookings. |
| `campaign_history` | Array | List of commercial advertising campaigns. |
| `media_upload_log` | Array | Timestamped log of media uploads requiring parental approval. |
| `booking_request_log` | Array | Timestamped log of public booking requests requiring parental approval. |
| `status` | Enum | `Active`, `Inactive`, `Archived`. |

## 2. Automation Workflows and Integration Points

### 2.1. Core Skill Commands

The skill will expose several commands via its `SKILL.md` to manage talent profiles:

* **`create_profile`**: Initializes a new talent profile based on the specified vertical and initial data.
  * Input: `talent_type` (Music Artist, Model, Child Model), `initial_data` (JSON object).
  * Output: `talent_id`, confirmation of profile creation.
* **`get_profile`**: Retrieves a full talent profile by `talent_id`.
  * Input: `talent_id`.
  * Output: Full talent profile (JSON object).
* **`update_profile`**: Modifies existing fields in a talent profile.
  * Input: `talent_id`, `updates` (JSON object with fields to update).
  * Output: Updated talent profile (JSON object).
* **`delete_profile`**: Archives or permanently deletes a talent profile.
  * Input: `talent_id`, `confirm_delete` (boolean).
  * Output: Confirmation of deletion/archiving.
* **`approve_child_media`**: Specifically for Child Models, sets `parental_approval` to `true` for a given media upload or booking request.
  * Input: `talent_id`, `request_id` (identifier for media/booking request).
  * Output: Confirmation of approval.

### 2.2. Integration with Dashboard (Conceptual)

While the skill itself will operate within Manus, its outputs and functionalities are designed to feed into the Entertainment Management Dashboard. This implies:

* **Data Export**: The skill could provide commands to export talent data in formats consumable by the dashboard (e.g., JSON, CSV).
* **Status Updates**: The skill could be triggered by events (e.g., new streaming data available) to update talent profiles, which then reflect in the dashboard.

### 2.3. Future Integration with CRM & Admin

* **Automated Reminders**: The skill could be extended to set calendar reminders (e.g., via Google Calendar API) for communication follow-ups or contract renewals.
* **Onboarding Forms**: Integration with form-building tools to generate and process initial digital onboarding questionnaires.

## 3. Development Roadmap

1. **Phase 1: Core Profile Management (MVP)**
   * Implement `create_profile`, `get_profile`, `update_profile`, `delete_profile` commands.
   * Establish file-based JSON storage for talent profiles.
   * Develop basic data validation for each talent vertical.
2. **Phase 2: Child Model Security Layer**
   * Implement `approve_child_media` command.
   * Develop the `parental_approval` logic and logging.
3. **Phase 3: Data Tracking & Reporting**
   * Add functionalities to aggregate and present key metrics (e.g., `get_streaming_report`, `get_follower_growth`).
   * Implement data parsing for external sources (e.g., mock streaming API integration).
4. **Phase 4: Dashboard Integration & UI Hooks (Conceptual)**
   * Define clear data export formats for dashboard consumption.
   * Explore mechanisms for real-time data synchronization (e.g., webhooks, API endpoints).

## References

[1] Entertainment Management Dashboard Specifications (V2). (n.d.). `/home/ubuntu/hh-client-vault/internal/talent-management/docs/dashboard-specifications.txt`
