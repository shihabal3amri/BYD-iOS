# BYD iOS Localized

**English · العربية · Русский**

Unofficial localization and navigation preferences for the Chinese BYD iPhone app. **Revision 2**, based on BYD **9.16.0**.

[**Add to AltStore Classic**](https://shihabal3amri.github.io/BYD-iOS/) · [**Download the IPA**](https://github.com/shihabal3amri/BYD-iOS/releases/tag/v9.16.0-r2) · [**Report a problem**](https://github.com/shihabal3amri/BYD-iOS/issues/new?template=beta-feedback.md)

**AltStore Classic must already be installed and configured.** This link adds the BYD catalogue; it does not install AltStore. There is no charge for this project or its downloads. This is not an AltStore PAL listing or a computer-free initial installation service.

## What's included

- Select English, Arabic or Russian in **Me → Settings → Language**.
- Hide or show **Discover**, **Mall** and **Service** separately in **Me → Settings → Bottom bar**.
- **My Car** uses BYD's original car icon instead of the Chinese brand artwork.
- Bluetooth badges appear on supported dashboard controls when the car is connected.
- Includes the existing launch, network-identity, post-login storage and translated-confirmation fixes.

Fully close BYD in the iPhone app switcher and reopen it after changing language. Bottom-bar changes take effect immediately. My Car and Me remain available.

<p>
  <img src="assets/language-en.png" alt="English language selector with English, Arabic and Russian options" width="260">
  <img src="assets/language-ru.png" alt="Russian language selector" width="260">
</p>

## Install or update

### Updating an existing installation

Open AltStore with AltServer running and reachable, let the source refresh, then choose **Update** for BYD under **My Apps**. Look for **9.16.0 · Revision 2** (build **202608311148**). Keep your existing app and use the same Apple account so its local data is retained. The IPA is about **339 MB**; download speed depends on your connection to GitHub.

### If AltStore Classic is already configured

1. Open the **Add to AltStore Classic** link above on your iPhone.
2. Confirm adding the **BYD iOS Localized** source.
3. Select **BYD Localized**, review its permissions, then install it with your own Apple account.
4. Open BYD and sign in to your own BYD account. The home-screen app name may still appear in Chinese.

If the link does not open AltStore, add this URL manually under **Browse → Sources → +**:

```text
https://raw.githubusercontent.com/shihabal3amri/BYD-iOS/main/source.json
```

For the normal AltStore Classic installation flow, AltServer must be reachable through the same Wi-Fi network or USB. Free Apple-account signing requires refreshing before the seven-day validity expires. See the [official AltServer guide](https://faq.altstore.io/altstore-classic/altserver).

### If AltStore Classic is not installed

Follow the official [macOS](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) or [Windows](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows) setup guide. Initial setup requires a computer, USB pairing, an Apple account and Developer Mode on iOS 16 or later.

As of **9 September 2026**, AltStore's remote-server mode is a Patreon-only beta and still requires initial computer setup. It is optional and is not required to download this project. See the [current remote-server instructions](https://faq.altstore.io/altstore-classic/no-computer-instructions).

### Install using Impactor

The underlying build has been tested with **Impactor 2.5.0 (formerly PlumeImpactor)**.

1. Download the IPA from the release and import it into [Impactor](https://github.com/claration/Impactor).
2. On the package options screen, replace the Chinese text in **Name** with **BYD**.
3. Sign/install with your own Apple account. Keep the normal team-suffixed bundle identifier and app-group handling. Do not force the original App Store bundle identifier or remove the app-group entitlement.

**If installation fails with Developer API error 35 / missing `appIdName`:** return to the package options, set **Name** to **BYD**, then retry. You can reuse the same IPA. Impactor 2.5.0 [keeps only ASCII letters when registering an app name](https://github.com/claration/Impactor/blob/v2.5.0/crates/plume_core/src/developer/mod.rs#L14-L17), so this IPA's original Chinese name becomes empty. Its Name option updates the bundle name before registration. This workaround is verified against the installer code; the reporting tester's successful installation is still pending.

This IPA must be re-signed by an installer. Downloading it in Safari alone will not install it.

## Compatibility and current status

- The package declares **iOS 15.0 or later** and targets iPhones. This is a packaging requirement, not a claim that every model or iOS release has been tested.
- The underlying code has **203 prior offline checks**. An Impactor-signed predecessor was installed on an iPhone X with iOS 16.7.16 and an iPhone XS with iOS 17.6.1. The final language/tab runtime audit was performed on the iPhone X.
- Normal public-source installation and startup through **AltStore Classic 2.2.2** were verified on an **iPhone XS / iOS 17.6.1**. The maintainer also reports successful tests on several other iPhones.
- Revision 2’s Bluetooth badge fix was reproduced and verified on the jailbroken iPhone X. Testing the new revision as an AltStore update on the XS is the next check.
- Revision 2 adds one existing BYD PNG at the dashboard’s expected resource path and increments the build number. Every other existing IPA entry, including all executable code and translations, is byte-identical to public beta 1. The public packaging keeps the executable's code/data sections and translation resources unchanged. It uses minimal sideloading entitlements, excludes personal provisioning profiles, and removes the old App Store model allow-list so newer iPhones can be tested.
- Chinese promotional artwork, some live content, unvisited screens and the About-page version prefix remain translation work.
- The profile page can show a blank screen. The same behavior was observed in the official iOS app and Android app; its cause remains unresolved.
- **Wakeup unlock is not included** in this release.
- Apple-restricted capabilities, including Wallet car keys, push notifications and Siri integration, are not promised for this sideloaded build. No claim is made that all vehicle functions have been validated on every account or vehicle.

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

The [release](https://github.com/shihabal3amri/BYD-iOS/releases/tag/v9.16.0-r2) includes the IPA, **SHA256SUMS**, and **verification.json**. [release.json](release.json) records the same package hash and validation status. The download is re-signable and contains no personal developer provisioning profile or device login data.

Maintainers can check catalogue/package consistency with:

```sh
python3 scripts/validate_source.py /path/to/BYD-iOS_9.16.0_r2.ipa
```

## Project status

This repository is the public download catalogue and feedback tracker. It does not claim ownership of BYD's original application or assets, and it is not affiliated with or endorsed by BYD. No license to BYD's proprietary code is granted by this repository.

The full translation goal remains active. Broader language review, remaining artwork and live content, and the later wakeup-unlock phase remain on the roadmap.
