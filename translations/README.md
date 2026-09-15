# Signed translation updates

Production feeds for compatible public builds:

- iOS: `channels/stable-ios.json`
- Android: `channels/stable-android.json`

Both currently serve signed revision 7. Clients download immutable `packs/<revision>/<platform>/payload.json`, verify the signature with their pinned public key and retain their previous translation if validation fails. Automatic updates default off. Manual downloads apply after fully closing and reopening the app. Widget translations on iOS remain bundled with the app.

Separate test channels use a separate test key and are not used by public builds. Never publish private signing keys, account data or device logs. Existing immutable revisions are retained.

Revision 7 adds the Ti7 EV Flash model name and spacing variants in English, Arabic, Russian and Spanish. Simplified Chinese retains the original text.
