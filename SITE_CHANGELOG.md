# Site changelog

This file records maintenance milestones. Git history remains the detailed, authoritative change record.

## 2026-09-25

- Added a concise homepage “What’s Included” section with current adult/child pricing, core proteins, $500 food minimum, and links to the full menu and booking flow.
- Added Bay Area SEO landing pages for San Jose, Fremont, Oakland, and Palo Alto.
- Added internal links from the San Francisco Bay Area hub and California service page to the new city pages.
- Added the new Bay Area city URLs to the sitemap.
- Created restore branch `backup/2026-09-25-pre-home-included-bay-area-seo` before these changes.
- Production merge commit: `25ffbac736277b615abffd057380cf562dff7daf` (PR #11).

## 2026-09-22

- Added neutral `hbl_lead` and `hbl_booking_request` dataLayer events on the booking flow so Google Ads / GTM can map conversions without changing the customer experience.
- Created restore branch `backup/2026-09-22-pre-google-tracking-hook` before this tracking change.
- Created restore branch `backup/2026-09-22-pre-booking-flow` before changing the live booking experience.
- Reworked `/book` into a three-step flow: date/area/guest count → contact capture → menu/final request.
- Website Lead is now captured after the customer provides date + contact information; the full booking request remains a separate final step.
- Customers can mark the menu as TBD and finalize proteins later instead of being forced to complete every protein selection before sending a request.
- Updated the Los Angeles landing page CTAs to “Check Availability” and routed the legacy Google Ads availability page into the unified booking flow while preserving ad query parameters.

## 2026-09-20

- Added Southern California city SEO pages and supporting internal links. Commit: `d3e616678f2c520c6dfc30bffabbf7905af8ab79`.
- Unified homepage SEO metadata and the canonical `www.hibachibylin.com` domain. Commit: `0dbd7a8cc64c0cd2ce0b029d6f0ed200cdf4c638`.
- Aligned the homepage social-sharing SEO description. Commit: `e888d5d5cdb0a22c57651979d042a9b3a63ec1dc`.
- Added the durable maintenance, recovery, and backup workflow for future Chat and Work sessions.

## 2026-09-25 — Booking flow address cleanup

- Moved the complete event address to Step 1: street, city, state and ZIP.
- Removed duplicate event-address entry from Step 3.
- Kept contact/date/time/address/allergy fields required and made protein selection required before submission.

## 2026-09-25 21:20 UTC — Event Moments gallery

- Added five portrait event photos and one playable portrait video to the homepage Event Moments carousel.
- Shows one item at a time with horizontal swipe and six synchronized navigation dots.
- Commit: see Git history for this entry.
