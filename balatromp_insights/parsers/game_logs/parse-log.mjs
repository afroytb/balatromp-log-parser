import { readFileSync } from 'fs'
import { parseLogSource } from './log-source-parser'
const games = await parseLogSource(readFileSync(process.argv[2], 'utf-8'))
console.log(JSON.stringify(games, 2))