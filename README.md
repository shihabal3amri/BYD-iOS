# BYD iOS Localized

[**English**](README.md) · [**العربية**](README.ar.md) · [**Русский**](README.ru.md)

Unofficial localization and navigation preferences for the Chinese BYD iPhone app. **Public beta · Revision 5**, based on BYD **9.16.0**. No jailbreak required.

The [download page](https://shihabal3amri.github.io/BYD-iOS/) also has English, Arabic and Russian language buttons.

[**Add to AltStore Classic**](https://shihabal3amri.github.io/BYD-iOS/) · [**Download the IPA**](https://github.com/shihabal3amri/BYD-iOS/releases/tag/v9.16.0-r5) · [**Report a problem**](https://github.com/shihabal3amri/BYD-iOS/issues/new?template=beta-feedback.md)

**AltStore Classic must already be installed and configured.** This link adds the BYD catalogue; it does not install AltStore. There is no charge for this project or its downloads. This is not an AltStore PAL listing or a computer-free initial installation service.

## New in Revision 5: startup stability

Fixes a crash when BYD tries to cache a widget image but shared storage is unavailable. Improves compatibility with installers that rename app groups. Includes the localized Home Screen and Lock Screen widgets from Revision 4.

When AltStore asks, choose **Keep App Extensions**. Open BYD after updating and leave it open for about 30 seconds, then add BYD widgets from the widget gallery. Existing widgets may take time to refresh; they follow your selected BYD language.

BYD includes four widget extensions: the app and extensions use five App IDs in total. Check available IDs in AltStore → My Apps → View App IDs. [AltStore explains the App ID limit.](https://faq.altstore.io/altstore-classic/app-ids)

## What's included

- Select English, Arabic or Russian in **Me → Settings → Language**.
- Hide or show **Discover**, **Mall** and **Service** separately in **Me → Settings → Bottom bar**.
- **My Car** uses BYD's original car icon instead of the Chinese brand artwork.
- Bluetooth badges appear on supported dashboard controls when the car is connected.
- Includes the existing launch, network-identity, post-login storage and translated-confirmation fixes.

Fully close BYD in the iPhone app switcher and reopen it after changing language. Bottom-bar changes take effect immediately. My Car and Me remain available.

<p>
  <a href="assets/dashboard-r2.png"><img src="assets/dashboard-r2.png" alt="My Car dashboard with restored Bluetooth badges on Lock, Windows, Engine Off, Trunk and AC" width="200"></a>
  <a href="assets/language-en.png"><img src="assets/language-en.png" alt="English language selector with English, Arabic and Russian options" width="200"></a>
  <a href="assets/bottom-bar-ar.png"><img src="assets/bottom-bar-ar.png" alt="Arabic bottom-bar settings for Discover, Mall and Service" width="200"></a>
  <a href="assets/language-ru.png"><img src="assets/language-ru.png" alt="Russian language selector" width="200"></a>
</p>

Actual iPhone screenshots: Revision 2's My Car dashboard, language selection and customizable bottom tabs. Select an image to view it full size.

## Install or update

### First-time AltStore setup

Install **AltServer on a Mac or Windows computer**, then use it to install **AltStore Classic on your iPhone**. Use **your own Apple account**; a paid developer membership is not required. Initial setup includes USB pairing and Developer Mode on iOS 16 or later.

- [Video tutorial in Arabic](https://youtu.be/05xOiC5TwQ8?si=iv-KIpAl5oyJoKnP)
- [Video tutorial in English](https://youtu.be/yLuyVakPpUM?si=QloJ8z-acfZEbB4v)
- Current official instructions: [macOS](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) · [Windows](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows)

The videos explain AltStore setup; screens and steps can vary by version. After setup, add BYD using the steps below.

### Updating an existing installation

Open AltStore with AltServer running and reachable, let the source refresh, then choose **Update** for BYD under **My Apps**. Look for **9.16.0 · Revision 5** (build **202608311172**). Keep your existing app and use the same Apple account so its local data is retained. The IPA is about **349 MB**; download speed depends on your connection to GitHub.

### If AltStore Classic is already configured

1. Open the **Add to AltStore Classic** link above on your iPhone.
2. Confirm adding the **BYD iOS Localized** source.
3. Select **BYD Localized**, review its permissions, then install it with your own Apple account.
4. Open BYD and sign in to your own BYD account. The app appears as BYD on the Home Screen.

If the link does not open AltStore, add this URL manually under **Browse → Sources → +**:

```text
https://raw.githubusercontent.com/shihabal3amri/BYD-iOS/main/source.json
```

For the normal AltStore Classic installation flow, AltServer must be running and reachable through the same Wi-Fi network or USB. With a free Apple account, refresh **both AltStore and BYD** before their seven-day signing period expires. You need AltServer for installing, updating and refreshing; it is not required simply to open BYD while its signature remains valid. See the [official AltServer guide](https://faq.altstore.io/altstore-classic/altserver).

### Install using Impactor

Import the IPA into [Impactor](https://github.com/claration/Impactor), keep the app name **BYD** and all widget extensions, then sign and install with your own Apple account. Keep the normal bundle-identifier and app-group handling. If Developer API error 35 mentions `appIdName`, check that Name is BYD and retry. Downloading the IPA alone does not install it.

## Walk-up unlock · optional beta

Open **Me → Settings → Walk-up unlock**. Unlock as you approach and optionally lock when walking away, using your already activated BYD Bluetooth key. Automatic actions, location support, movement hints and test recording are **off by default for new users**. Private testers retain their saved settings.

1. Confirm BYD’s normal Bluetooth Lock/Unlock works. Open **Choose your distances**, measure both positions with your phone where you normally carry it, then save. Automatic actions are paused while calibration is open.
2. Enable **Walk-up unlock** and optionally **Lock when walking away**. Start away from the car, approach, then walk away and check what the car actually does. Calibrate every phone separately.
3. For locked-screen use, open **Background detection → Location support**, follow the permission prompts and use **Allow background location** when offered. **Movement hints** is optional and requests Motion & Fitness. Reopen BYD after a phone restart or force-closing the app.

Background support may increase battery use; uninterrupted or overnight operation is not guaranteed. This feature processes location on the phone and does not save or upload coordinates. Other BYD location features have their own settings.

**Known XS issue:** one iPhone XS produced inconsistent signal readings, with an unintended indoor unlock reported during earlier testing. The inconsistent readings persisted after updating to iOS 18.7.10. The cause is unresolved; a hardware fault is not established. If near/far readings overlap or unintended actions occur, turn Walk-up unlock off and report it.

For feedback, enable Test logs before testing, mark important moments and export afterward. Include your phone/iOS, vehicle model, thresholds, screen state and actual car response. Review logs before sharing publicly.

[Report walk-up behavior](https://github.com/shihabal3amri/BYD-iOS/issues/new?template=walkup-feedback.md)

## Compatibility and current status

The storage crash was reproduced and the fix passed focused macOS and iOS laboratory tests, including loading the complete production module without app-group entitlements. The exact R5 app still needs confirmation on affected non-jailbroken phones, including iOS 27 beta. An installation failure reported separately remains undiagnosed.

Requires iOS 15 or later. Testing does not yet cover every phone, vehicle or overnight scenario. The reported XS proximity issue remains unresolved. Some Chinese content and artwork remain; the profile page may be blank.

Existing English, Arabic and Russian localization, configurable tabs and Bluetooth badges remain included. Some Chinese content and the shared blank profile page remain unresolved. Push notifications, Wallet car keys and other Apple-restricted capabilities are unavailable or unverified in this sideloaded app. Previous public-source installation and launch were verified through AltStore Classic on the XS.

## Testing and feedback

1. Report the iPhone model, iOS version, installer/version and release revision.
2. Confirm installation and whether BYD stays open.
3. Sign in normally and check the tutorial, My Car and Settings navigation.
4. Check each language, fully restarting between changes.
5. Check that hiding each optional tab preserves navigation and saved preferences.
6. Report any crash, untranslated text or layout issue through [GitHub Issues](https://github.com/shihabal3amri/BYD-iOS/issues/new?template=beta-feedback.md). Please include whether a problem occurred during a fresh install, update or refresh.

Use the same Apple account and installer bundle identity for subsequent updates to preserve local app data. Avoid uninstalling when applying an update.

Please remove account details, phone numbers, VINs, location, device identifiers and tokens from screenshots or logs before posting them publicly. Apple-account credentials belong in the installer, never in a GitHub issue.

## Downloads and verification

The [release](https://github.com/shihabal3amri/BYD-iOS/releases/tag/v9.16.0-r5) includes the IPA, **SHA256SUMS**, and **verification.json**. [release.json](release.json) records the same package hash and validation status. The download is re-signable and contains no personal developer provisioning profile or device login data.

Maintainers can check catalogue/package consistency with:

```sh
python3 scripts/validate_source.py /path/to/BYD-iOS_9.16.0_r5.ipa
```

## Project status

This repository is the public download catalogue and feedback tracker. It does not claim ownership of BYD's original application or assets, and it is not affiliated with or endorsed by BYD. No license to BYD's proprietary code is granted by this repository.

The full translation goal remains active. Further language review, remaining content and broader walk-up beta testing continue.
