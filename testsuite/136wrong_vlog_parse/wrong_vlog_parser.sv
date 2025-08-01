module wrong_vlog_parser;
  bit clk;
  bit big_arr [32];

  always_comb
    dumb_function_one(arg1, arg2);

  always_ff @(posedge clk)
    dumb_function_two(arg1, arg2);

  always_ff @(posedge clk) begin
    assert (clk == 0);
  end

  initial begin
    foreach (big_arr[i])
      big_arr[i] = (1);
  end

endmodule : wrong_vlog_parser
