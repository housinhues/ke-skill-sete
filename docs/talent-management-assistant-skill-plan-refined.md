# Implementation Plan: Talent Management Assistant Skill (Refined)

## Introduction

This refined implementation plan for the **Talent Management Assistant Skill** focuses on specific talent verticals crucial to Housing Hues: Hip Hop Artists, Amapiano Dancers, Models, Stylists, and Event Curators. It also incorporates the current roster and the agency structure, with a clear understanding that Manus will facilitate agentic operations under Housing Hues, led by Nate Mongale.

## 1. Core Architecture and Data Models

### 1.1. Skill Definition (`SKILL.md`)

The `SKILL.md` will define the skill's purpose, core functionalities, input parameters, and expected outputs, serving as the primary interface for interaction.

### 1.2. Data Persistence Strategy

Initial implementation will use file-based storage (e.g., JSON files within the skill's directory) for talent profiles, allowing for rapid prototyping. Future enhancements will explore integration with external database APIs.

### 1.3. Talent Data Models (Refined)

Each talent vertical will have a distinct data model, capturing specific metrics and attributes. These models will be represented as structured data (e.g., JSON objects) within the skill's storage.

#### 1.3.1. Hip Hop Artist Profile Model

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the artist. |
| `name` | String | Artist's stage name or group name (e.g., Music Xhefs). |
| `type` | Enum | `Solo` or `Duo/Group`. |
| `genre` | String | Primary music genre (e.g., Hip Hop). |
| `name_registries` | Array | List of registered names (e.g., SAMRO, ASCAP, BMI). |
| `streaming_counters`| Object | Key-value pairs for streaming platforms (e.g., `spotify: 1.2M`). |
| `follower_counts` | Object | Key-value pairs for social media platforms (e.g., `instagram: 500K`). |
| `contact_info` | Object | Email, phone, manager contact. |
| `status` | Enum | `Active`, `On Hiatus`, `Archived`. |

#### 1.3.2. Amapiano Dancer Profile Model

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the dancer. |
| `name` | String | Dancer's stage name or full name (e.g., Keabetswe Moleme). |
| `style` | String | Specific dance style (e.g., Amapiano). |
| `portfolio_links` | Array | Links to dance reels, performance videos. |
| `social_media` | Object | Key-value pairs for social media platforms (e.g., `tiktok: 1M`). |
| `contact_info` | Object | Email, phone, agent contact. |
| `status` | Enum | `Active`, `Booked`, `Unavailable`. |

#### 1.3.3. Model Profile Model

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the model. |
| `name` | String | Model's full name (e.g., Amogelang Mogale, Junior Tau). |
| `gender` | Enum | `Male`, `Female`, `Other`. |
| `physical_stats` | Object | Height, weight, measurements, eye color, hair color. |
| `portfolio_specs` | Array | Links to portfolio, comp cards. |
| `lookbook_registries`| Array | List of associated lookbooks. |
| `brand_ambassador_contracts` | Array | List of active brand ambassador contracts. |
| `agency_representations` | Array | List of agencies representing the model. |
| `contact_info` | Object | Email, phone, agent contact. |
| `status` | Enum | `Active`, `Inactive`, `Archived`. |

#### 1.3.4. Stylist Profile Model

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the stylist. |
| `name` | String | Stylist's full name. |
| `specialization` | Array | Areas of expertise (e.g., `fashion`, `editorial`, `personal`). |
| `portfolio_links` | Array | Links to styling portfolio. |
| `contact_info` | Object | Email, phone. |
| `status` | Enum | `Active`, `Booked`, `Unavailable`. |

#### 1.3.5. Event Curator Profile Model

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the event curator. |
| `name` | String | Curator's full name. |
| `specialization` | Array | Types of events curated (e.g., `music festivals`, `corporate`, `private`). |
| `past_events` | Array | List of notable past events with roles. |
| `contact_info` | Object | Email, phone. |
| `status` | Enum | `Active`, `Planning`, `Executing`. |

#### 1.3.6. Creative Professional Profile Model (for Concept Generator, Photographer)

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `talent_id` | String | Unique identifier for the professional. |
| `name` | String | Professional's full name (e.g., School boy, Lebohang Mosolodi). |
| `role` | String | Specific role (e.g., `Concept Generator`, `Photographer`). |
| `specialization` | Array | Areas of expertise (e.g., `conceptual art`, `portrait photography`). |
| `portfolio_links` | Array | Links to portfolio. |
| `contact_info` | Object | Email, phone. |
| `status` | Enum | `Active`, `Project-based`, `Unavailable`. |

#### 1.3.7. Agency/Business Entity Profile Model (for Housing Hues, 018 Production, Thapelo)

| Field Name | Data Type | Description |
| :------------------ | :-------- | :-------------------------------------------------------------------------- |
| `entity_id` | String | Unique identifier for the entity. |
| `name` | String | Entity name (e.g., Housing Hues, 018 Production, Thapelo). |
| `type` | Enum | `Agency`, `Production Company`, `Business Acumen`. |
| `contact_info` | Object | Email, phone, primary contact. |
| `services` | Array | List of services offered (e.g., `creative direction`, `media production`). |
| `partnerships` | Array | List of associated partners/clients. |
| `agentic_facilitator` | String | Name of the agentic facilitator (e.g., Nate Mongale). |

## 2. Automation Workflows and Integration Points

### 2.1. Core Skill Commands (Updated)

The skill will expose commands to manage these refined talent and entity profiles:

* **`create_profile`**: Initializes a new profile based on the specified vertical/type and initial data.
  * Input: `profile_type` (Hip Hop Artist, Amapiano Dancer, Model, Stylist, Event Curator, Creative Professional, Agency/Business Entity), `initial_data` (JSON object).
  * Output: `profile_id`, confirmation of profile creation.
* **`get_profile`**: Retrieves a full profile by `profile_id`.
  * Input: `profile_id`.
  * Output: Full profile (JSON object).
* **`update_profile`**: Modifies existing fields in a profile.
  * Input: `profile_id`, `updates` (JSON object with fields to update).
  * Output: Updated profile (JSON object).
* **`delete_profile`**: Archives or permanently deletes a profile.
  * Input: `profile_id`, `confirm_delete` (boolean).
  * Output: Confirmation of deletion/archiving.

### 2.2. Initial Roster Integration

The skill will be initialized with the following profiles:

* **Models:**
  * Amogelang Mogale (Female Model)
  * Junior Tau (Male Model)
* **Hip Hop Artists:**
  * Music Xhefs (Duo)
* **Creative Professionals:**
  * School boy (Concept Generator)
  * Lebohang Mosolodi (Photographer)
* **Amapiano Dancers:**
  * Keabetswe Moleme
* **Agency/Business Entities:**
  * Thapelo (Business Management acumen)
  * 018 Production (Media Production Co.)
  * Housing Hues (Creative & Operational Agency, Agentic Facilitation by Nate Mongale)

### 2.3. Integration with Dashboard (Conceptual)

Outputs and functionalities are designed to feed into the Entertainment Management Dashboard, providing data export and status updates.

### 2.4. Future Integration with CRM & Admin

Automated reminders and onboarding forms will be explored for future enhancements.

## 3. Development Roadmap

1. **Phase 1: Core Profile Management (MVP)**
   * Implement `create_profile`, `get_profile`, `update_profile`, `delete_profile` commands for all defined verticals.
   * Establish file-based JSON storage for profiles.
   * Develop basic data validation.
2. **Phase 2: Roster Initialization & Refinement**
   * Pre-populate the skill with the initial roster data.
   * Refine data models based on real-world usage and feedback.
3. **Phase 3: Data Tracking & Reporting**
   * Add functionalities to aggregate and present key metrics relevant to each vertical.
   * Implement data parsing for external sources (e.g., social media APIs for follower counts).
4. **Phase 4: Dashboard Integration & UI Hooks (Conceptual)**
   * Define clear data export formats for dashboard consumption.
   * Explore mechanisms for real-time data synchronization.

## References

[1] Entertainment Management Dashboard Specifications (V2). (n.d.). `/home/ubuntu/hh-client-vault/internal/talent-management/docs/dashboard-specifications.txt`
