/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        visa: {
          free: '#10b981',     // emerald-500
          evisa: '#0ea5e9',    // sky-500
          voa: '#f59e0b',      // amber-500
          required: '#ef4444', // red-500
        }
      }
    },
  },
  plugins: [],
}

