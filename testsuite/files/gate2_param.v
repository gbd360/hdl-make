module gate2#(parameter int INV = 0)(input i, output o);
  assign o = INV ? ~i : i;
endmodule
