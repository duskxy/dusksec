from django import template

register = template.Library()


@register.filter(name="css", is_safe=True)
def css_filter(form, css):
    if 'class' in form.field.widget.attrs:
        form.field.widget.attrs['class'] += " %s" % css
    else:
        form.field.widget.attrs['class'] = css

    return form


@register.filter(name="placeholder", is_safe=True)
def placeholder_filter(form, default=""):
    text = default if default else form.label
    if 'placeholder' not in form.field.widget.attrs:
        form.field.widget.attrs['placeholder'] = text

    return form

@register.filter(name="first_error", is_safe=True)
def first_error_filter(errors):
    if not errors:
        return errors

    if 'captcha' in errors:
        data = errors['captcha'].as_text()
    else:
        data = errors.get(tuple(errors)[0]).as_text()

    return data
