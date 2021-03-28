Home Assistant integration Marshall smartspeakers.


**Note: this is a work in progress**, a lot of functionality is
missing or not fully working!

## Installation
Install the `custom_components/marshall` directory of this repo to your
Home Assistant `custom_components` directory. See the [Home Assistant docs] for details.

## Configuration
**Note: Currently only YAML-based configuration is supported.**

Add a section like the following to your Home Assistant config.yaml:

```
marshall:
  addresses: 
    - <network address>
```

You will need the following items of information:
* The network address of your Marshall smart speaker.

See [CHANGELOG.md](./CHANGELOG.md) for release notes.

## TODO
* Tests
* CI
* Docs
* config_flow (only configured via yaml for now)

[Home Assistant docs]: https://developers.home-assistant.io/docs/creating_integration_file_structure
