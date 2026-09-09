# Changes

## 9.16.0 · Revision 2 — 9 September 2026

Bluetooth badges now appear on supported dashboard controls when the car is connected, including Lock, Windows, Engine Off and Trunk on the tested vehicle.

The dashboard was already choosing to show the badges, but its image lookup returned no image. This update places BYD’s existing badge PNG at the expected resource path. All executable code, Bluetooth connection checks, vehicle-control behavior and translations are unchanged.

Update through the existing AltStore source: refresh the source, then choose **Update** for BYD in **My Apps**. Look for **9.16.0 · Revision 2**, build **202608311148**. Keep your existing installation and use the same Apple account.

The fix was reproduced and visually verified on the jailbroken iPhone X. The previous public release installed and launched successfully through AltStore Classic on an iPhone XS; the new revision’s AltStore update test follows publication.

[Installation guide](https://shihabal3amri.github.io/BYD-iOS/) · [Report a problem](https://github.com/shihabal3amri/BYD-iOS/issues)

The release includes the re-signable IPA, SHA256SUMS and verification.json. Existing limitations remain: some Chinese content/artwork, the shared blank profile page, deferred wakeup unlock, and unavailable Apple-restricted capabilities such as push notifications.

## 9.16.0 · Public beta 1

First public source release with English, Arabic and Russian, configurable bottom tabs and My Car icon.
