def format_tfvar(tfvar):
    if isinstance(tfvar, str):
        return f'"{tfvar}"'

    if isinstance(tfvar, dict):
        return tfvar

    if isinstance(tfvar, list):
        joined_list = '", "'.join(tfvar)
        return f'[ "{joined_list}" ]'

    return tfvar

class FilterModule(object):
    def filters(self):
        filters = {
            'format_tfvar': format_tfvar
        }

        return filters
