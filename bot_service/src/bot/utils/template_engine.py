from typing import Sequence

from jinja2 import Environment, PackageLoader

jinja_env = Environment(
    loader=PackageLoader("bot.multimedia", "templates"),
    autoescape=True,
    lstrip_blocks=True,
    trim_blocks=True
)


def render_template(name: str, **kwargs) -> str:
    template = jinja_env.get_template(name)
    return template.render(**kwargs)


def pluralize(value: str, variants: Sequence[str]) -> str:
    """
    :param value: value to pluralize
    :param variants: variants of forms
    :return: pluralized value
    """

    int_value = int(value)

    if int_value % 10 == 1 and int_value % 100 != 11:
        variant_idx = 0
    elif 2 <= int_value % 10 <= 4 and \
            (int_value % 100 < 10 or int_value % 100 >= 20):
        variant_idx = 1
    else:
        variant_idx = 2

    return variants[variant_idx]


jinja_env.filters["pluralize"] = pluralize
