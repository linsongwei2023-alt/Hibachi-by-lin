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

## 2026-09-26 03:00 UTC — Event Moments mobile size

- Reduced the portrait media carousel width on phones based on the visible viewport height, so one item fits more comfortably on screen without cropping.
- Commit: see Git history for this entry.

## 2026-09-26 03:04 UTC — Wider Event Moments on phones

- Changed the phone gallery frame to a wider 2:3 portrait shape with centered media cropping, while keeping the six original files and carousel behavior.
- Commit: see Git history for this entry.

## 2026-09-26 03:14 UTC — Fixed 3:4 portrait Event Moments frame

- Set every Event Moments slide to a 3:4 width-to-height frame (portrait orientation of the camera's 4:3 setting).
- Photos and videos display in full within the frame; future 3:4 portrait photos fill it naturally, while narrower videos retain side space.
- Commit: see Git history for this entry.

## 2026-09-26 03:19 UTC — Replace Event Moments media

- Replaced the five gallery photos and video with the new user-provided 3:4 versions in the same order.
- Refreshed the video poster and gallery media URLs to avoid stale browser caches. No other page content or carousel behavior changed.
- Commit: see Git history for this entry.

## 2026-09-26 04:20 UTC — Homepage typography

- Simplified the hero headline and supporting sentence while keeping the mobile hibachi service description.
- Balanced the homepage typography across phone and desktop: smaller introductory label, consistent section headings, and more readable card, step, FAQ and note text.
- Kept the existing black-and-gold design, section order, booking links and behavior.
- Commit: 67a0fdcaa78bdb08df1579ede35aa9ca7d1e5453.

## 2026-09-26 04:34 UTC — Sitewide typography

- Added a shared typography stylesheet to all 31 interior HTML pages, including service areas, city landing pages, menu, booking, quote, review and availability.
- Standardized heading hierarchy and line spacing, increased small body and form text, and retained existing page content and behavior.
- Commit: see Git history for this entry.

## 2026-09-26 04:43 UTC — Homepage entrance animation

- Added a short black-and-gold first-visit intro using the existing logo and a fire-inspired light sweep.
- Intro is skippable, plays once per browser tab session, and is omitted for reduced-motion settings.
- Kept homepage content, booking links, and other pages unchanged.
- Commit: see Git history for this entry.
