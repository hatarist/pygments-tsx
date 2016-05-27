from pygments.lexers.javascript import TypeScriptLexer


class TypeScriptXLexer(TypeScriptLexer):
    name = 'TypeScriptX'
    aliases = ['tsx', 'typescriptx']
    filenames = ['*.tsx']
