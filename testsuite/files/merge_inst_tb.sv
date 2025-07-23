module merge_inst_tb;
  reg i, o;

  gate2#(.INV(0))dut(.i(i), .o(o));

  initial begin
    i <= 0;
    # 1;
    $stop;
  end
endmodule
