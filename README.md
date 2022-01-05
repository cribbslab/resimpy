# Resimpy

Resimpy Documentation https://resimpy.readthedocs.io/en/latest/index.html

```angular2html
 ____           _                         _____           _ _    _ _
|  _ \ ___  ___(_)_ __ ___  _ __  _   _  |_   _|__   ___ | | | _(_) |_
| |_) / _ \/ __| | '_ ` _ \| '_ \| | | |   | |/ _ \ / _ \| | |/ / | __|
|  _ <  __/\__ \ | | | | | | |_) | |_| |   | | (_) | (_) | |   <| | |_
|_| \_\___||___/_|_| |_| |_| .__/ \__, |   |_|\___/ \___/|_|_|\_\_|\__|
                           |_|    |___/

 _    _      _
| |  | |    | |
| |  | | ___| | ___ ___  _ __ ___   ___
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \
\  /\  /  __/ | (_| (_) | | | | | |  __/
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|



```

```angular2html
# resimpy_general seq_errs 
resimpy_general -r seq_errs -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -seq_errs 1e-3;1e-2;0.1 -out_dir ./

# resimpy_general pcr_errs
resimpy_general -r pcr_errs -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_errs 1e-3;1e-2;0.1 -out_dir ./

# resimpy_general ampl_rates 
resimpy_general -r ampl_rates -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -ampl_rates 0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;1.0 -out_dir ./

# resimpy_general pcr_nums
resimpy_general -r pcr_nums -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_nums 6;7;8;9;10;11;12;13;14 -out_dir ./

# resimpy_general umi_lens
resimpy_general -r umi_lens -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -umi_lens 6;7;8;9;10;11;12 -out_dir ./
```

