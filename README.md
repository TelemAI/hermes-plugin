# Telem plugin for Hermes Agent

Adds two tools to [Hermes Agent](https://github.com/NousResearch/hermes-agent):

- `telem_search` — web search across Telem's providers, several queries in one call.
- `telem_fetch` — read the full text of web pages.

## Install

```bash
hermes plugins install TelemAI/hermes-plugin
hermes plugins enable telem
```

Hermes installs the `telem-sdk` Python package for you. Set your API key from the
[Telem console](https://app.telem.ai) as `TELEM_API_KEY`.

The plugin needs Hermes 0.21.6 or newer, installed with the
[official Hermes installer](https://github.com/NousResearch/hermes-agent#quick-install).
Homebrew builds of Hermes cannot install the plugin
([NousResearch/hermes-agent#126711](https://github.com/NousResearch/hermes-agent/issues/126711)).

## Documentation

Configuration, auto-routing and troubleshooting:
[docs.telem.ai/integrations/hermes](https://docs.telem.ai/integrations/hermes/).

## License

Apache-2.0
