# 📊 Product Analytics Tracking Specification
### *LITTLE BLUEPRINT: Event Taxonomy & Conversion Funnels*
*Conforming to `analytics-tracking-spec` Standards (PostHog, Segment, Mixpanel)*

---

## 1. Event Taxonomy Standard: Object-Action Syntax

All events use lowercase snake_case with explicit `[Object] [Action in Past Tense]` naming:

| Event Name | Trigger Moment | Key Properties Included |
| :--- | :--- | :--- |
| `quiz_started` | User taps "Begin Quiz" on landing page | `source_campaign`, `utm_medium`, `device_type` |
| `quiz_step_completed` | User finishes step 1, 2, 3, or 4 | `step_number`, `step_name`, `time_spent_seconds` |
| `child_profile_created` | Birth time, date, and city submitted | `child_age_months`, `has_exact_time`, `country` |
| `blueprint_revealed` | Free archetype screen loaded | `nakshatra_name`, `zodiac_sign`, `element` |
| `paywall_viewed` | Annual subscription or book offer shown | `paywall_type`, `presented_plan`, `currency` |
| `trial_started` | User confirms 3-day free trial on iOS/Web | `plan_id` (`annual_79_99`), `trial_duration_days` |
| `subscription_activated` | First paid charge clears (Day 4) | `plan_id`, `amount_usd`, `payment_method` |
| `keepsake_book_ordered` | User purchases physical hardcover book | `order_id`, `amount_usd`, `shipping_country` |
| `daily_score_checked` | User opens app and views sensory gauge | `score_value`, `alert_level`, `day_of_week` |
| `crisis_script_viewed` | Parent taps to expand a gentle script | `script_id`, `elemental_pairing`, `trigger_topic` |
| `doula_message_sent` | Parent submits a question to Doula AI | `session_id`, `character_count`, `context_type` |

---

## 2. Standard Event Payload Schema

Every event tracked across web, iOS, and backend services must include standard contextual properties:

```json
{
  "event": "trial_started",
  "properties": {
    "distinct_id": "usr_c89f21b",
    "child_id": "chd_982b14",
    "plan_id": "annual_sub_79_99",
    "amount_usd": 79.99,
    "currency": "USD",
    "is_annual": true,
    "platform": "ios_native",
    "app_version": "1.0.0",
    "source_campaign": "tiktok_sensory_hook_q4",
    "timestamp_utc": "2026-10-18T22:45:00Z"
  }
}
```

---

## 3. Core Conversion Funnels to Instrument in PostHog

### Funnel 1: Web-to-App Acquisition Funnel
1. `landing_page_viewed`
2. `quiz_started`
3. `quiz_step_completed` (Step 4: Parenting Struggles)
4. `child_profile_created`
5. `blueprint_revealed`
6. `paywall_viewed`
7. `trial_started` (Target conversion: >12% of quiz completions)

### Funnel 2: Keepsake Book Gifting Funnel
1. `book_landing_viewed`
2. `book_preview_customized`
3. `checkout_initiated`
4. `keepsake_book_ordered` (Target conversion: >8% of organic visitors)

### Funnel 3: Core Retention & Engagement Loop (DAU)
1. `app_opened`
2. `daily_score_checked`
3. `crisis_script_viewed` OR `doula_message_sent`
