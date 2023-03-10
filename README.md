# Mimeo

**Mimeo** (Mimeograph) is a tool generating XML data based on a template.

E.g.  

**Template**
```json
{
  "count": 2,
  "model": {
    "attributes": {
      "xmlns": "http://data-generator.arch.com/default-namespace",
      "xmlns:pn": "http://data-generator.arch.com/prefixed-namespace"
    },
    "SomeEntity": {
      "ChildNode1": 1,
      "ChildNode2": "value-2",
      "ChildNode3": true
    }
  }
}
```

**XML Data**
```xml
<SomeEntity xmlns="http://data-generator.arch.com/default-namespace" xmlns:pn="http://data-generator.arch.com/prefixed-namespace">
    <ChildNode1>1</ChildNode1>
    <ChildNode2>value-2</ChildNode2>
    <ChildNode3>true</ChildNode3>
</SomeEntity>
```
```xml
<SomeEntity xmlns="http://data-generator.arch.com/default-namespace" xmlns:pn="http://data-generator.arch.com/prefixed-namespace">
    <ChildNode1>1</ChildNode1>
    <ChildNode2>value-2</ChildNode2>
    <ChildNode3>true</ChildNode3>
</SomeEntity>
```

Mimeo exposes several functions for data generation that will make it more useful for testing purposes.

E.g.  

**Template**
```json
{
  "count": 2,
  "model": {
    "attributes": {
      "xmlns": "http://data-generator.arch.com/default-namespace"
    },
    "SomeEntity": {
      "id": "{auto_increment()}",
      "randomstring": "{random_str()}",
      "randomint": "{random_int()}",
    }
  }
}
```

**XML Data**
```xml
<SomeEntity xmlns="http://data-generator.arch.com/default-namespace">
    <id>00001</id>
    <randomstring>mCApsYZprayYkmKnYWxe</randomstring>
    <randomint>8</randomint>
</SomeEntity>
```
```xml
<SomeEntity xmlns="http://data-generator.arch.com/default-namespace">
    <id>00003</id>
    <randomstring>ceaPUqARUkFukZIPeuqO</randomstring>
    <randomint>2</randomint>
</SomeEntity>
```

## Mimeo configuration

Mimeo configuration is defined in a json file including internal settings and data templates.  
You can find several examples in the `examples` folder.

### Internal settings

|               Key               |  Level   |      Required      | Supported values |    Default     | Description                                                              |
|:-------------------------------:|:--------:|:------------------:|:----------------:|:--------------:|--------------------------------------------------------------------------|
|         `output_format`         |  Config  |        :x:         |      `xml`       |     `xml`      | Defines output data format                                               |
|        `output_details`         |  Config  |        :x:         |      object      |      ---       | Defines output details on how it will be consumed                        |
|   `output_details/direction`    |  Config  |        :x:         |      `file`      |     `file`     | Defines how output will be consumed                                      |
| `output_details/directory_path` |  Config  |        :x:         |      string      | `mimeo-output` | For `file` direction - defines an output directory                       |
|   `output_details/file_name`    |  Config  |        :x:         |      string      | `mimeo-output` | For `file` direction - defines an output file name                       |
|            `indent`             |  Config  |        :x:         |     integer      |     `null`     | Defines indent applied in output data                                    |
|        `xml_declaration`        |  Config  |        :x:         |     boolean      |    `false`     | Indicates whether an xml declaration should be added to output data      |
|          `_templates_`          |  Config  | :heavy_check_mark: |      array       |      ---       | Stores templates for data generation                                     |
|             `count`             | Template | :heavy_check_mark: |     integer      |      ---       | Indicates number of copies                                               |
|             `model`             | Template | :heavy_check_mark: |      object      |      ---       | Defines data template to be copied                                       |
|          `attributes`           |  Model   |        :x:         |      object      |      ---       | Defines attributes applied on the root node (mostly used for namespaces) |