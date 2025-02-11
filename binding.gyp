{
    'targets': [
        {
            'target_name': 'native',
            'dependencies': [
                "<!(node -p \"require('node-addon-api').gyp\")",
            ],
            'sources': [
                'c++/_.cc',
            ],
            # Use pre-built libs
            'include_dirs': [
                "<!@(node -p \"require('node-addon-api').include\")",
            ],
            'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
            'libraries': [
                # References LVML
                '<!@(ldconfig -p | grep "libnvidia-ml.so " | sed -n -e "s/^.* => \\(.*\\)$/\\1/p" | head -n 1)',
            ],
            'conditions': [
                ['OS=="mac"', {
                    'libraries': [],
                }],
            ],
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'cflags_cc': [
                '-std=c++17',
                '-fexceptions',
                '-fpermissive',
                '-Wall',
                '-O3',
            ],
        },
    ],
}
