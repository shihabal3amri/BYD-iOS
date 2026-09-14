# Translation update test channel

Signed translation data for compatible iOS and Android test builds. These feeds do not update the app executable and do not change the public R5 app release.

- iOS: `channels/test-ios.json`
- Android: `channels/test-android.json`
- Payloads: immutable `packs/<revision>/<platform>/payload.json`

Clients pin the verification public key. Private signing keys are never published here. Automatic updates default off; manual downloads activate after reopening the app. Revision 3 adds an English test marker to translation settings help. No stable translation feed is published yet.
