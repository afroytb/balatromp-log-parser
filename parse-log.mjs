import { readFileSync } from 'fs'
import { parseLogSource } from './json_parser/log-source-parser'
const games = await parseLogSource(readFileSync(process.argv[2] ||
  './var/lovely-2026.05.25-17.34.03.log', 'utf-8'))
console.log(JSON.stringify(games, 2))