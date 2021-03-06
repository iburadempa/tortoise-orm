from tortoise import Tortoise, fields
from tortoise.contrib import test
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    events: fields.ReverseRelation["Event"]

    class Meta:
        ordering = ["name"]


class Event(Model):
    """
    The Event model docstring.

    This is multiline docs.
    """

    id = fields.IntField(pk=True)
    #: The Event NAME
    #:  It's pretty important
    name = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    tournament: fields.ForeignKeyNullableRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events", null=True
    )

    class Meta:
        ordering = ["name"]


class TestBasic(test.TestCase):
    def test_early_init(self):

        self.maxDiff = None
        Event_TooEarly = pydantic_model_creator(Event)
        self.assertEqual(
            Event_TooEarly.schema(),
            {
                "title": "Event",
                "type": "object",
                "description": "The Event model docstring.<br/><br/>This is multiline docs.",
                "properties": {
                    "id": {"title": "Id", "type": "integer"},
                    "name": {
                        "title": "Name",
                        "type": "string",
                        "description": "The Event NAME<br/>It's pretty important",
                    },
                    "created_at": {"title": "Created At", "type": "string", "format": "date-time"},
                },
            },
        )
        self.assertEqual(
            Tortoise.describe_model(Event),
            {
                "name": "None.",
                "app": None,
                "table": "",
                "abstract": False,
                "description": "The Event model docstring.",
                "docstring": "The Event model docstring.\n\nThis is multiline docs.",
                "unique_together": [],
                "pk_field": {
                    "name": "id",
                    "field_type": "IntField",
                    "db_column": "id",
                    "db_field_types": {"": "INT"},
                    "python_type": "int",
                    "generated": True,
                    "nullable": False,
                    "unique": True,
                    "indexed": True,
                    "default": None,
                    "description": None,
                    "docstring": None,
                },
                "data_fields": [
                    {
                        "name": "name",
                        "field_type": "TextField",
                        "db_column": "name",
                        "db_field_types": {"": "TEXT", "mysql": "LONGTEXT"},
                        "python_type": "str",
                        "generated": False,
                        "nullable": False,
                        "unique": False,
                        "indexed": False,
                        "default": None,
                        "description": "The Event NAME",
                        "docstring": "The Event NAME\nIt's pretty important",
                    },
                    {
                        "name": "created_at",
                        "field_type": "DatetimeField",
                        "db_column": "created_at",
                        "db_field_types": {"": "TIMESTAMP", "mysql": "DATETIME(6)"},
                        "python_type": "datetime.datetime",
                        "generated": False,
                        "nullable": False,
                        "unique": False,
                        "indexed": False,
                        "default": None,
                        "description": None,
                        "docstring": None,
                    },
                ],
                "fk_fields": [
                    {
                        "name": "tournament",
                        "field_type": "ForeignKeyFieldInstance",
                        "raw_field": None,
                        "python_type": "None",
                        "generated": False,
                        "nullable": True,
                        "unique": False,
                        "indexed": False,
                        "default": None,
                        "description": None,
                        "docstring": None,
                    }
                ],
                "backward_fk_fields": [],
                "o2o_fields": [],
                "backward_o2o_fields": [],
                "m2m_fields": [],
            },
        )

        Tortoise.init_models(["tests.test_early_init"], "models")

        Event_Pydantic = pydantic_model_creator(Event)
        self.assertEqual(
            Event_Pydantic.schema(),
            {
                "title": "Event",
                "type": "object",
                "description": "The Event model docstring.<br/><br/>This is multiline docs.",
                "properties": {
                    "id": {"title": "Id", "type": "integer"},
                    "name": {
                        "title": "Name",
                        "type": "string",
                        "description": "The Event NAME<br/>It's pretty important",
                    },
                    "created_at": {"title": "Created At", "type": "string", "format": "date-time"},
                    "tournament": {
                        "title": "Tournament",
                        "allOf": [{"$ref": "#/definitions/Tournament"}],
                    },
                },
                "definitions": {
                    "Tournament": {
                        "title": "Tournament",
                        "type": "object",
                        "properties": {
                            "id": {"title": "Id", "type": "integer"},
                            "name": {"title": "Name", "type": "string"},
                            "created_at": {
                                "title": "Created At",
                                "type": "string",
                                "format": "date-time",
                            },
                        },
                    }
                },
            },
        )
        self.assertEqual(
            Tortoise.describe_model(Event),
            {
                "name": "models.Event",
                "app": "models",
                "table": "event",
                "abstract": False,
                "description": "The Event model docstring.",
                "docstring": "The Event model docstring.\n\nThis is multiline docs.",
                "unique_together": [],
                "pk_field": {
                    "name": "id",
                    "field_type": "IntField",
                    "db_column": "id",
                    "db_field_types": {"": "INT"},
                    "python_type": "int",
                    "generated": True,
                    "nullable": False,
                    "unique": True,
                    "indexed": True,
                    "default": None,
                    "description": None,
                    "docstring": None,
                },
                "data_fields": [
                    {
                        "name": "name",
                        "field_type": "TextField",
                        "db_column": "name",
                        "db_field_types": {"": "TEXT", "mysql": "LONGTEXT"},
                        "python_type": "str",
                        "generated": False,
                        "nullable": False,
                        "unique": False,
                        "indexed": False,
                        "default": None,
                        "description": "The Event NAME",
                        "docstring": "The Event NAME\nIt's pretty important",
                    },
                    {
                        "name": "created_at",
                        "field_type": "DatetimeField",
                        "db_column": "created_at",
                        "db_field_types": {"": "TIMESTAMP", "mysql": "DATETIME(6)"},
                        "python_type": "datetime.datetime",
                        "generated": False,
                        "nullable": False,
                        "unique": False,
                        "indexed": False,
                        "default": None,
                        "description": None,
                        "docstring": None,
                    },
                    {
                        "name": "tournament_id",
                        "field_type": "IntField",
                        "db_column": "tournament_id",
                        "db_field_types": {"": "INT"},
                        "python_type": "int",
                        "generated": False,
                        "nullable": True,
                        "unique": False,
                        "indexed": False,
                        "default": None,
                        "description": None,
                        "docstring": None,
                    },
                ],
                "fk_fields": [
                    {
                        "name": "tournament",
                        "field_type": "ForeignKeyFieldInstance",
                        "raw_field": "tournament_id",
                        "python_type": "models.Tournament",
                        "generated": False,
                        "nullable": True,
                        "unique": False,
                        "indexed": False,
                        "default": None,
                        "description": None,
                        "docstring": None,
                    }
                ],
                "backward_fk_fields": [],
                "o2o_fields": [],
                "backward_o2o_fields": [],
                "m2m_fields": [],
            },
        )
