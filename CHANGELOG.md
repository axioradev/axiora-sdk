# Changelog

## 0.11.0 (2026-05-07)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/axioradev/axiora-sdk/compare/v0.10.0...v0.11.0)

### Features

* add subsidiaries and shareholding-audit endpoints ([9ca7183](https://github.com/axioradev/axiora-sdk/commit/9ca7183ae7f23c98eaae482ca189828fc70700be))
* **api:** add is_consolidaed to FinancialOut ([b2d9e3e](https://github.com/axioradev/axiora-sdk/commit/b2d9e3e034d22cdf4921abff6023eaa5e0d59510))
* **api:** add sections api endpoints ([5b92006](https://github.com/axioradev/axiora-sdk/commit/5b92006a558abedb9c355ffa6b3118dcfe5753e7))
* **api:** manual updates ([1b5e6f9](https://github.com/axioradev/axiora-sdk/commit/1b5e6f9d699fb4a0736ed2cfd1d217b279d4e9d9))
* **api:** manual updates ([12b1545](https://github.com/axioradev/axiora-sdk/commit/12b1545475416bff5375163ff683e97a58b489c4))
* **api:** manual updates ([4ca4df3](https://github.com/axioradev/axiora-sdk/commit/4ca4df3ce1b9e56f755270b0a1af4849ec5a5036))
* **api:** manual updates ([8352e0d](https://github.com/axioradev/axiora-sdk/commit/8352e0d5681790bb33bcf322a810064b025f1fe7))
* **api:** manual updates ([ac38e70](https://github.com/axioradev/axiora-sdk/commit/ac38e7077476c9684d23fcc587f6a8440d701f28))
* **api:** section endpoints ([9cc9e74](https://github.com/axioradev/axiora-sdk/commit/9cc9e7429f22203f0dc4b949167037b7e81b37d2))
* extend Company, Financial, SectorListItem, and Meta types ([ccb6d59](https://github.com/axioradev/axiora-sdk/commit/ccb6d597f251c3dec5570221bf3732e54a6984cf))
* **internal:** implement indices array format for query and form serialization ([7e1133e](https://github.com/axioradev/axiora-sdk/commit/7e1133ebffba77a7748150c8fa216bd405f801b4))
* **ontology:** add resource for queryable field metadata ([a556381](https://github.com/axioradev/axiora-sdk/commit/a556381dbd4b80641a6dcd4979ff962fadfdd9d4))
* support setting headers via env ([472629b](https://github.com/axioradev/axiora-sdk/commit/472629b19a45f76191746c9d0b499c33ddd8c6d2))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([12bceb9](https://github.com/axioradev/axiora-sdk/commit/12bceb9f72be0fe19a9c6c441b158efe1bf9265b))
* **deps:** bump minimum typing-extensions version ([5431e43](https://github.com/axioradev/axiora-sdk/commit/5431e43887cc36ae681299d8a1ca061f21a1a1ef))
* ensure file data are only sent as 1 parameter ([dbbdbda](https://github.com/axioradev/axiora-sdk/commit/dbbdbda4ad6feaf8aba6803152738cbfdbffa43b))
* **pydantic:** do not pass `by_alias` unless set ([00361df](https://github.com/axioradev/axiora-sdk/commit/00361df4d3bf01affd8644882edab79f626bddb4))
* sanitize endpoint path params ([8cb29f7](https://github.com/axioradev/axiora-sdk/commit/8cb29f7dc5d40f630245c10d49099a1af9cdaa3f))
* use correct field name format for multipart file arrays ([10667a8](https://github.com/axioradev/axiora-sdk/commit/10667a8b3f19cf456d8ebfb0b6c79b2bcaf026e9))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([c9abccd](https://github.com/axioradev/axiora-sdk/commit/c9abccd83e7e8fcc72e585f24de613c3fd6cef52))


### Chores

* **ci:** bump uv version ([cb1c955](https://github.com/axioradev/axiora-sdk/commit/cb1c955033e49f690dc017c5363417608f342975))
* **ci:** skip lint on metadata-only changes ([a6e3968](https://github.com/axioradev/axiora-sdk/commit/a6e3968eb64fca555b4f27a5470a68eb21787a5e))
* **ci:** skip uploading artifacts on stainless-internal branches ([cd61b0e](https://github.com/axioradev/axiora-sdk/commit/cd61b0e5d792c140aeaea78d09c66ceb8926c3a3))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([9fcbdd7](https://github.com/axioradev/axiora-sdk/commit/9fcbdd703ac269e87ca130856b330f9fcd2da43f))
* **internal:** more robust bootstrap script ([0dee67b](https://github.com/axioradev/axiora-sdk/commit/0dee67b2852c6174305f3e4bdb6fbecaeaeec783))
* **internal:** refactor authentication internals ([e2069e2](https://github.com/axioradev/axiora-sdk/commit/e2069e263b8fb9b738dcfda660c4e292fc8f79aa))
* **internal:** reformat pyproject.toml ([504892c](https://github.com/axioradev/axiora-sdk/commit/504892cfd0926bd9f93e2449a83cd9372a8bb014))
* **internal:** tweak CI branches ([7c5d3c1](https://github.com/axioradev/axiora-sdk/commit/7c5d3c1106d9768e9caca1acea8f040a3f02f19a))
* **internal:** update gitignore ([ca5cd8c](https://github.com/axioradev/axiora-sdk/commit/ca5cd8c240c1c84b846eab16a134e1b7f43f50cb))
* regenerate openapi.json — add earnings, investors, watchlist, ownership chart endpoints ([d03f181](https://github.com/axioradev/axiora-sdk/commit/d03f181489ae588b7a1f24a14bd912f66d55972d))
* **release:** 0.10.0 ([4e2ca86](https://github.com/axioradev/axiora-sdk/commit/4e2ca86f249527d994c65c3a9c7dd712b524d335))
* sync repo ([0304381](https://github.com/axioradev/axiora-sdk/commit/03043810581737b145fc39626ab1509527e4d34b))
* update SDK settings ([cee414e](https://github.com/axioradev/axiora-sdk/commit/cee414ecf848b71dc1e5c4f74ad57a79868e8834))
* update SDK settings ([4d1ea9f](https://github.com/axioradev/axiora-sdk/commit/4d1ea9f2f2c067852d4b4db689a8f093dd033181))
* update SDK settings ([622f5f7](https://github.com/axioradev/axiora-sdk/commit/622f5f74f3a67500dd0437d41a36afca747a2d80))
* update SDK settings ([6c69d33](https://github.com/axioradev/axiora-sdk/commit/6c69d3300bf11f367b6080fdeee788bbbfe6866e))
* update SDK settings ([6a915cc](https://github.com/axioradev/axiora-sdk/commit/6a915ccae58b24cbd4f29f447b5604bc0e165cb2))
* update SDK settings ([81f7667](https://github.com/axioradev/axiora-sdk/commit/81f766736bec0ae015f1f3331ade01a4de2b87bf))
* update SDK settings ([a6510c8](https://github.com/axioradev/axiora-sdk/commit/a6510c8153050aebc7ec1d99cae089d64d33755b))
* update SDK settings ([0124007](https://github.com/axioradev/axiora-sdk/commit/0124007014e77792fea11e92e510a6f5078a7584))
* update SDK settings ([db38a9e](https://github.com/axioradev/axiora-sdk/commit/db38a9ead622087522dc18634d99475b774a5565))


### Documentation

* rewrite README product-first and update api.md ([7666543](https://github.com/axioradev/axiora-sdk/commit/7666543de454cfb03bdde6b02c201a36368f5325))

## 0.10.0 (2026-05-07)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/axioradev/axiora-sdk/compare/v0.9.0...v0.10.0)

### Features

* **Company**: add `sector_display` (always-populated label — `'Unlisted'` when listing is null, `'Uncategorised'` when listed but unclassified, otherwise the English sector name) and `entity_type` fields.
* **Financial**: add derived ratios `roa`, `operating_margin`, `net_margin`, `gross_margin`, `equity_ratio` — computed in-band from raw inputs when not stored, never null when the inputs are present.
* **Financial**: expose `accounting_standard` ('JP-GAAP' / 'IFRS' / 'US-GAAP'), `explanations` (per-field null reasons), and `sources` (XBRL provenance) on the response model.
* **SectorListItem**: add `sector_display` matching the Company field.
* **Meta**: add `computation_version`, `ontology_version`, and `data_as_of` fields for response provenance.
* **Companies**: add `client.companies.retrieve_subsidiaries(code, limit=...)` — subsidiary registry from the parent's annual 関係会社 disclosure with bidirectional `cross_validation` outcomes (`bidirectional_match` / `voting_pct_mismatch` / `parent_only`).
* **Shareholdings**: add `client.shareholdings.retrieve_audit(shareholding_id)` — per-row provenance bundle (source filing + real-time classification + retrospective label + classifier version stamp).
* **Ontology** (new resource): `client.ontology.retrieve_version()`, `client.ontology.list_fields(category=...)`, `client.ontology.retrieve_field(field_name)` — queryable metadata for every field in the API, with per-accounting-standard mappings (JP-GAAP / IFRS / US-GAAP).
* **Subsidiary** type docstrings now enumerate the possible values for `cross_validation` and `relationship_type` so SDK users see the contract inline.

### Breaking Changes

* **Financial.roe** now returns percentage units (e.g. `13.6` for 13.6%) across the entire dataset. Previously ~99.8% of stored values were raw fractions (`0.136`) inconsistent with the schema contract. The unit fix is enforced at the API; SDK consumers receive normalised values without code changes — but anyone who multiplied `roe * 100` for display must remove that step.


Full Changelog: [v0.8.2...v0.9.0](https://github.com/axioradev/axiora-sdk/compare/v0.8.2...v0.9.0)

### Features

* support setting headers via env ([472629b](https://github.com/axioradev/axiora-sdk/commit/472629b19a45f76191746c9d0b499c33ddd8c6d2))


### Bug Fixes

* use correct field name format for multipart file arrays ([10667a8](https://github.com/axioradev/axiora-sdk/commit/10667a8b3f19cf456d8ebfb0b6c79b2bcaf026e9))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([c9abccd](https://github.com/axioradev/axiora-sdk/commit/c9abccd83e7e8fcc72e585f24de613c3fd6cef52))


### Chores

* **internal:** more robust bootstrap script ([0dee67b](https://github.com/axioradev/axiora-sdk/commit/0dee67b2852c6174305f3e4bdb6fbecaeaeec783))
* **internal:** reformat pyproject.toml ([504892c](https://github.com/axioradev/axiora-sdk/commit/504892cfd0926bd9f93e2449a83cd9372a8bb014))

## 0.8.2 (2026-04-12)

Full Changelog: [v0.8.1...v0.8.2](https://github.com/axioradev/axiora-sdk/compare/v0.8.1...v0.8.2)

### Chores

* regenerate openapi.json — add earnings, investors, watchlist, ownership chart endpoints ([d03f181](https://github.com/axioradev/axiora-sdk/commit/d03f181489ae588b7a1f24a14bd912f66d55972d))

## 0.8.1 (2026-04-11)

Full Changelog: [v0.8.0...v0.8.1](https://github.com/axioradev/axiora-sdk/compare/v0.8.0...v0.8.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([12bceb9](https://github.com/axioradev/axiora-sdk/commit/12bceb9f72be0fe19a9c6c441b158efe1bf9265b))
* ensure file data are only sent as 1 parameter ([dbbdbda](https://github.com/axioradev/axiora-sdk/commit/dbbdbda4ad6feaf8aba6803152738cbfdbffa43b))

## 0.8.0 (2026-03-31)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/axioradev/axiora-sdk/compare/v0.7.0...v0.8.0)

### Features

* **api:** manual updates ([1b5e6f9](https://github.com/axioradev/axiora-sdk/commit/1b5e6f9d699fb4a0736ed2cfd1d217b279d4e9d9))

## 0.7.0 (2026-03-31)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/axioradev/axiora-sdk/compare/v0.6.0...v0.7.0)

### Features

* **api:** manual updates ([12b1545](https://github.com/axioradev/axiora-sdk/commit/12b1545475416bff5375163ff683e97a58b489c4))

## 0.6.0 (2026-03-27)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/axioradev/axiora-sdk/compare/v0.5.0...v0.6.0)

### Features

* **internal:** implement indices array format for query and form serialization ([7e1133e](https://github.com/axioradev/axiora-sdk/commit/7e1133ebffba77a7748150c8fa216bd405f801b4))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([5431e43](https://github.com/axioradev/axiora-sdk/commit/5431e43887cc36ae681299d8a1ca061f21a1a1ef))
* **pydantic:** do not pass `by_alias` unless set ([00361df](https://github.com/axioradev/axiora-sdk/commit/00361df4d3bf01affd8644882edab79f626bddb4))
* sanitize endpoint path params ([8cb29f7](https://github.com/axioradev/axiora-sdk/commit/8cb29f7dc5d40f630245c10d49099a1af9cdaa3f))


### Chores

* **ci:** skip lint on metadata-only changes ([a6e3968](https://github.com/axioradev/axiora-sdk/commit/a6e3968eb64fca555b4f27a5470a68eb21787a5e))
* **ci:** skip uploading artifacts on stainless-internal branches ([cd61b0e](https://github.com/axioradev/axiora-sdk/commit/cd61b0e5d792c140aeaea78d09c66ceb8926c3a3))
* **internal:** refactor authentication internals ([e2069e2](https://github.com/axioradev/axiora-sdk/commit/e2069e263b8fb9b738dcfda660c4e292fc8f79aa))
* **internal:** tweak CI branches ([7c5d3c1](https://github.com/axioradev/axiora-sdk/commit/7c5d3c1106d9768e9caca1acea8f040a3f02f19a))
* **internal:** update gitignore ([ca5cd8c](https://github.com/axioradev/axiora-sdk/commit/ca5cd8c240c1c84b846eab16a134e1b7f43f50cb))

## 0.5.0 (2026-03-03)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/axioradev/axiora-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** add sections api endpoints ([5b92006](https://github.com/axioradev/axiora-sdk/commit/5b92006a558abedb9c355ffa6b3118dcfe5753e7))
* **api:** section endpoints ([9cc9e74](https://github.com/axioradev/axiora-sdk/commit/9cc9e7429f22203f0dc4b949167037b7e81b37d2))


### Chores

* **ci:** bump uv version ([cb1c955](https://github.com/axioradev/axiora-sdk/commit/cb1c955033e49f690dc017c5363417608f342975))

## 0.4.0 (2026-02-26)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/axioradev/axiora-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** manual updates ([4ca4df3](https://github.com/axioradev/axiora-sdk/commit/4ca4df3ce1b9e56f755270b0a1af4849ec5a5036))

## 0.3.0 (2026-02-26)

Full Changelog: [v0.2.1...v0.3.0](https://github.com/axioradev/axiora-sdk/compare/v0.2.1...v0.3.0)

### Features

* **api:** add is_consolidaed to FinancialOut ([b2d9e3e](https://github.com/axioradev/axiora-sdk/commit/b2d9e3e034d22cdf4921abff6023eaa5e0d59510))

## 0.2.1 (2026-02-25)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/axioradev/axiora-sdk/compare/v0.2.0...v0.2.1)

### Chores

* **internal:** make `test_proxy_environment_variables` more resilient to env ([9fcbdd7](https://github.com/axioradev/axiora-sdk/commit/9fcbdd703ac269e87ca130856b330f9fcd2da43f))

## 0.2.0 (2026-02-25)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/axioradev/axiora-sdk/compare/v0.1.0...v0.2.0)

### Features

* **api:** manual updates ([8352e0d](https://github.com/axioradev/axiora-sdk/commit/8352e0d5681790bb33bcf322a810064b025f1fe7))

## 0.1.0 (2026-02-25)

Full Changelog: [v0.0.3...v0.1.0](https://github.com/axioradev/axiora-sdk/compare/v0.0.3...v0.1.0)

### Features

* **api:** manual updates ([ac38e70](https://github.com/axioradev/axiora-sdk/commit/ac38e7077476c9684d23fcc587f6a8440d701f28))

## 0.0.3 (2026-02-24)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/axioradev/axiora-sdk/compare/v0.0.2...v0.0.3)

### Chores

* update SDK settings ([cee414e](https://github.com/axioradev/axiora-sdk/commit/cee414ecf848b71dc1e5c4f74ad57a79868e8834))
* update SDK settings ([4d1ea9f](https://github.com/axioradev/axiora-sdk/commit/4d1ea9f2f2c067852d4b4db689a8f093dd033181))

## 0.0.2 (2026-02-24)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/axioradev/axiora-sdk/compare/v0.0.1...v0.0.2)

### Chores

* sync repo ([0304381](https://github.com/axioradev/axiora-sdk/commit/03043810581737b145fc39626ab1509527e4d34b))
* update SDK settings ([622f5f7](https://github.com/axioradev/axiora-sdk/commit/622f5f74f3a67500dd0437d41a36afca747a2d80))
* update SDK settings ([6c69d33](https://github.com/axioradev/axiora-sdk/commit/6c69d3300bf11f367b6080fdeee788bbbfe6866e))
* update SDK settings ([6a915cc](https://github.com/axioradev/axiora-sdk/commit/6a915ccae58b24cbd4f29f447b5604bc0e165cb2))
* update SDK settings ([81f7667](https://github.com/axioradev/axiora-sdk/commit/81f766736bec0ae015f1f3331ade01a4de2b87bf))
* update SDK settings ([a6510c8](https://github.com/axioradev/axiora-sdk/commit/a6510c8153050aebc7ec1d99cae089d64d33755b))
* update SDK settings ([0124007](https://github.com/axioradev/axiora-sdk/commit/0124007014e77792fea11e92e510a6f5078a7584))
* update SDK settings ([db38a9e](https://github.com/axioradev/axiora-sdk/commit/db38a9ead622087522dc18634d99475b774a5565))
