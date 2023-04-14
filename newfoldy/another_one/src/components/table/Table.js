import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}

const rows = [
  createData('Savings Account', 1590, 6.0, 138.00, 1725.81),
  createData('Rent', 1075, 0.0, 0.0, 1075),
  createData('Checking Account', 262, 2.0, 5.24, 267.24),
  createData('Credit Debt', 305, 3.7, 11.28, 316.3),
  createData('Student Loans', 3956, 3, 118.68, 4074.68),
];

export default function DenseTable() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell> (Projected)</TableCell>
            <TableCell align="right">Current </TableCell>
            <TableCell align="right">Interest &nbsp;(%)</TableCell>
            <TableCell align="right">Total&nbsp;(g)</TableCell>
            <TableCell align="right">Upcoming&nbsp;($)</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.calories}</TableCell>
              <TableCell align="right">{row.fat}</TableCell>
              <TableCell align="right">{row.carbs}</TableCell>
              <TableCell align="right">{row.protein}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}