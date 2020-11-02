import React from "react";
import "./styles.css";

import { makeStyles } from "@material-ui/core/styles";
import Box from "@material-ui/core/Box";
import Collapse from "@material-ui/core/Collapse";

import IconButton from "@material-ui/core/IconButton";

import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";

import Typography from "@material-ui/core/Typography";

import Paper from "@material-ui/core/Paper";
import KeyboardArrowDownIcon from "@material-ui/icons/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@material-ui/icons/KeyboardArrowUp";




function getFileList() {
    return fetch("http://localhost:8080/file_list")
    .then((fileList) => fileList.json())
}
function getFileAnalysis(filename) {
    filename = filename.split(".")[0];
  
    return fetch(`http://localhost:8080/process/${filename}`)
      .then((f) => f.json())
      .catch((err) => {
        console.error(err);
        return { error: err };
      });
  }


  const useRowStyles = makeStyles({
    root: {
      "& > *": {
        borderBottom: "unset",
      },
    },
  });

export class Fileview extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
    };
  }

  async componentDidMount() {
    await getFileList()
      .then((fileList) => {
        const files = fileList.map((f) => ({ name: f, analysis: {} }));
        this.setState({ files }, async () => {
          const fileAnalysis = this.state.files.map((file) =>
            getFileAnalysis(file.name).then((analysis) => {
              return { name: file.name, analysis };
            })
          );
          const filesUpdate = await Promise.all(fileAnalysis);
          this.setState({ files: filesUpdate });
        });
      });
  }

  render() {
    return (
      <div style={{ width: "80vw", margin: "0 auto" }}>
        <br />

        <TableContainer component={Paper}>
          <Table aria-label="collapsible table">
            <TableHead>
              <TableRow>
                <TableCell />
                <TableCell>File name</TableCell>
                
              </TableRow>
            </TableHead>
            <TableBody>
              {this.state.files.map((row) => (
                <Row key={row.name} row={row} />
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    );
  }


}



function Row(props) {
  const { row } = props;
  const [open, setOpen] = React.useState(false);
  const classes = useRowStyles();

  return (
    <React.Fragment>
      <TableRow className={classes.root}>
        <TableCell>
          <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => setOpen(!open)}
          >
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </TableCell>
        <TableCell component="th" scope="row">
          {row.name}
        </TableCell>
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box margin={1}>
              <Typography variant="h6" gutterBottom component="div">
                Analysis
              </Typography>
              <Table size="small" aria-label="analysis">
                <TableHead>
                  <TableRow>
                    <TableCell>Function</TableCell>
                    <TableCell>Calling convention</TableCell>
                    <TableCell align="right">Return type</TableCell>
                    <TableCell align="right">Number of instructions</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {row &&
                    row.analysis &&
                    row.analysis.length > 0 &&
                    row.analysis.map((analysisRow) => (
                      <TableRow key={analysisRow.function}>
                        <TableCell component="th" scope="row">
                          {analysisRow.function}
                        </TableCell>
                        <TableCell>{analysisRow.cconv}</TableCell>
                        <TableCell align="right">
                          {analysisRow.rettype}
                        </TableCell>
                        <TableCell align="right">{analysisRow.isns}</TableCell>
                      </TableRow>
                    ))}
                </TableBody>
              </Table>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </React.Fragment>
  );
}
