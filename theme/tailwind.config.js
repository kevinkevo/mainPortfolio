module.exports = {
    darkMode: 'class', // Enable dark mode with a class toggle
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                purple: {
                    500: '#A855F7',
                    600: '#9333EA',
                },
                yellow: {
                    400: '#FBBF24',
                },
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
};