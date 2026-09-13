# Changes

## 9.16.0 · Revision 5 — 13 September 2026

Public beta · **9.16.0 · Revision 5** · build **202608311172**

- Fixes a startup/login crash when a widget image is saved without an available shared-storage path.
- Resolves the accessible signed app group even when the installer names it differently from the app ID. If shared storage is unavailable, optional image caching returns a failure safely.
- Includes all R4 widgets, English/Arabic/Russian translations and optional walk-up features. The app name remains **BYD**; the storage bug also existed before the rename.

**Validation:** reproduced the `NSData writeToFile` exception and verified the guards, signed-group variants and normal saves on macOS and in an iOS 16.7.16 laboratory harness. A separate iOS test loaded the complete production module without app-group entitlements and passed. Package checks preserve all R4 contents except five storage-module copies and five build-number plists. The exact R5 app has not yet been installed or launched on a non-jailbroken phone, and reporter confirmation—including iOS 27 beta—is pending. The separate “Unable to install” report remains undiagnosed.

**Update:** refresh the existing AltStore Classic source and choose **Update** for BYD. Keep the same Apple account, existing app and all four extensions. Widgets require working shared app-group permissions from the installer. Open BYD for about 30 seconds after updating.

**العربية:** إصلاح انهيار التطبيق عند حفظ صور الويدجت إذا لم تتوفر مساحة التخزين المشتركة، وتحسين التوافق مع أسماء مجموعات التطبيق بعد التوقيع. يتضمن جميع ميزات R4. اجتاز اختبارات مركّزة، وما زال تأكيده على الهواتف المتأثرة دون جيلبريك معلقًا. حدّث من AltStore مع الاحتفاظ بالتطبيق وإضافاته وحساب Apple نفسه.

**Русский:** исправлен сбой при сохранении изображений виджетов без доступного общего хранилища; улучшена обработка групп приложения после переподписания. Все функции R4 сохранены. Целевые тесты пройдены; подтверждение на затронутых телефонах без джейлбрейка ещё ожидается. Обновите BYD через AltStore, сохранив приложение, расширения и прежнюю учётную запись Apple.

[Install/update guide](https://shihabal3amri.github.io/BYD-iOS/) · [العربية](https://shihabal3amri.github.io/BYD-iOS/ar/) · [Русский](https://shihabal3amri.github.io/BYD-iOS/ru/)

## 9.16.0 · Revision 4 — 12 September 2026

Public beta · **9.16.0 · Revision 4** · build **202608311171**

- Restores Home Screen and Lock Screen widgets, including control icons and English, Arabic and Russian text.
- Fixes widget command errors caused by the phone’s time zone, and displays update times locally.
- Restores missing dashboard tile icons and fixes clipped widget mileage.
- Improves widget refresh after updates and language changes. Removes the private test name and development logging.

**Update:** refresh the existing AltStore Classic source, choose **Update** for BYD, and select **Keep App Extensions** when asked. Use the same Apple account and keep your installed app. Open BYD for about 30 seconds afterward; widgets may take time to refresh. The app and four extensions use five App IDs. [About AltStore App IDs](https://faq.altstore.io/altstore-classic/app-ids).

Home widgets are available with the app on iOS 15 or later; Lock Screen widgets require iOS 16 or later. Widget data and controls were confirmed during private testing on a stock XS. The final mileage-spacing correction passed focused rendering checks in all three languages; the exact public build’s on-device update remains to be confirmed. Package checks verified all four extensions, shared-group declarations and absence of personal profiles or device data.

The existing optional Walk-up unlock beta is included unchanged. Its previously reported XS proximity issue remains unresolved.

[Install/update guide](https://shihabal3amri.github.io/BYD-iOS/) · [العربية](https://shihabal3amri.github.io/BYD-iOS/ar/) · [Русский](https://shihabal3amri.github.io/BYD-iOS/ru/)

## 9.16.0 · Revision 3 — 11 September 2026

Public beta · **9.16.0 · Revision 3** · build **202608311159**

Adds optional **Walk-up unlock** and **Lock when walking away**, using your already activated BYD Bluetooth key. Includes English, Arabic and Russian settings, distance calibration, manual signal thresholds, optional background location and movement support, and local test logs with event marks and export.

### Set up

1. Confirm BYD's normal Bluetooth key and Lock/Unlock controls work for your car.
2. Open **Me → Settings → Walk-up unlock → Choose your distances**. Measure both positions with the phone where you normally carry it, then save. Automatic actions are paused while calibration is open.
3. Enable **Walk-up unlock** and, if wanted, **Lock when walking away**. These are off by default for new users. Begin testing away from the car, then approach and walk away; confirm the car's actual response.
4. For locked-screen testing, enable **Background detection → Location support**, follow the location permission prompts, and use **Allow background location** when offered. **Movement hints** is optional and uses Motion & Fitness. Background support can increase battery use; no indefinite or overnight guarantee is made. Reopen BYD after restarting the phone or force-closing the app.

### Test status and known issue

The identical walk-up code completed **six unlocks and six locks on a stock iPhone 12 Pro Max**, including three of each during a recorded locked/background interval. Earlier iterations also worked on the jailbroken iPhone X. This is limited field testing, not validation of every phone, vehicle or overnight scenario.

**One iPhone XS produced inconsistent signal readings, with an unintended indoor unlock reported during earlier testing. The inconsistent readings persisted after updating to iOS 18.7.10; the cause is unresolved, and a hardware fault has not been established.** If near/far readings overlap or an unintended action occurs, turn Walk-up unlock off and report it. Calibrate each phone separately; do not copy another phone's thresholds.

In **Test logs**, enable recording before a test, mark important moments, and export afterward. Logs are optional and stored locally. Include phone model, iOS, vehicle model, thresholds, whether the screen was locked and what the car actually did in a [walk-up feedback report](https://github.com/shihabal3amri/BYD-iOS/issues/new?template=walkup-feedback.md). Review logs and screenshots before sharing; never post account credentials, keys, VINs or signing files.

### Update

With AltServer running and reachable, refresh the existing AltStore Classic source and choose **Update** for BYD in **My Apps**. Keep the installed app and use the same Apple account. Look for **9.16.0 · Revision 3**, build **202608311159**. Existing private-test settings are retained; default-off applies when no walk-up settings exist.

The IPA contains the tested private revision 10 payload with only its build metadata incremented for this public update. It includes no personal signing profile or device data. AltStore re-signs it with your account. The public R3 AltStore update itself still awaits user confirmation.

[Installation and setup guide](https://shihabal3amri.github.io/BYD-iOS/) · [العربية](https://shihabal3amri.github.io/BYD-iOS/ar/) · [Русский](https://shihabal3amri.github.io/BYD-iOS/ru/)

Existing localization and dashboard badge features remain included. Some Chinese content and the shared blank profile page remain unresolved. Push notifications and other Apple-restricted capabilities remain unavailable or unverified for this sideloaded app.

## 9.16.0 · Revision 2 — 9 September 2026

Bluetooth badges now appear on supported dashboard controls when the car is connected, including Lock, Windows, Engine Off and Trunk on the tested vehicle.

The dashboard was already choosing to show the badges, but its image lookup returned no image. This update places BYD’s existing badge PNG at the expected resource path. All executable code, Bluetooth connection checks, vehicle-control behavior and translations are unchanged.

Update through the existing AltStore source: refresh the source, then choose **Update** for BYD in **My Apps**. Look for **9.16.0 · Revision 2**, build **202608311148**. Keep your existing installation and use the same Apple account.

The fix was reproduced and visually verified on the jailbroken iPhone X. The previous public release installed and launched successfully through AltStore Classic on an iPhone XS; the new revision’s AltStore update test follows publication.

[Installation guide](https://shihabal3amri.github.io/BYD-iOS/) · [Report a problem](https://github.com/shihabal3amri/BYD-iOS/issues)

The release includes the re-signable IPA, SHA256SUMS and verification.json. Existing limitations remain: some Chinese content/artwork, the shared blank profile page, deferred wakeup unlock, and unavailable Apple-restricted capabilities such as push notifications.

## 9.16.0 · Public beta 1

First public source release with English, Arabic and Russian, configurable bottom tabs and My Car icon.
